import requests, json, os
from bs4 import BeautifulSoup
from typing import TypedDict
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    name: str
    wikipedia_link: str
    flag_url: str

class Leader(TypedDict):
    name: str
    wikipedia_link: str
    image_url: str
    title: str
    # start_date: str
    # end_date: str
    states: list[State]

states: list[State] = []

def table_scrape(id: str, soup: BeautifulSoup, exists: list[str]) -> tuple[list[Leader], list[str]]:
    leaders: list[Leader] = []
    links_list: list[str] = []
    current_monarchs = soup.find(id=id)
    # go up to find the tbody
    tbody = current_monarchs.parent.parent.parent
    # find all tr
    trs = tbody.find_all('tr')
    for tr in trs:
        # check fi there is a td
        tds = tr.find_all('td')
        if len(tds) > 0:
            # check if tds[0] has class 'navbox-abovebelow'
            if 'navbox-abovebelow' in tds[0]['class']:
                continue
            ul = tds[0].find('div').find('ul')
            if ul is not None:
                lis = ul.find_all('li')
                for li in lis:
                    leader_states: list[State] = []
                    states = li.find_all('span', class_='flagicon')
                    for state in states:
                        # print(state.find('span').find('a'))
                        state_a = state.find('span').find('a')
                        state_name = state_a['title']
                        state_link = state_a['href'][2:]
                        state_flag = 'https:' + state_a.find('img')['src']
                        leader_states.append({
                            'name': state_name,
                            'wikipedia_link': state_link,
                            'flag_url': state_flag
                        })


                    a_tags = li.find('span').find_all('a', rel='mw:WikiLink')
                    for a in a_tags:
                        link = a['href'][2:]
                        links_list.append(link)

                        if link in exists:
                            continue

                        name = a.text

                        leader_info_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={a['href'][2:]}&prop=pageimages|pageterms&format=json&pithumbsize=1000"

                        print(leader_info_url)
                        
                        leader_info = requests.get(leader_info_url)

                        leader_info_json = leader_info.json()

                        leader_core = leader_info_json['query']['pages'][list(leader_info_json['query']['pages'].keys())[0]]

                        if 'thumbnail' not in leader_core:
                            leader_image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Portrait_Placeholder.png/600px-Portrait_Placeholder.png'
                        else: 
                            leader_image = leader_core['thumbnail']['source']

                        if 'terms' not in leader_core or 'description' not in leader_core['terms']:
                            leader_title = 'Unknown'
                        else:
                            leader_title = leader_core['terms']['description'][0]

                        leaders.append({
                            'name': name,
                            'wikipedia_link': link,
                            'image_url': leader_image,
                            'title': leader_title,
                            'states': leader_states
                        })

    return leaders, links_list

                    
def scrape(exists: list[str]) -> tuple[list[Leader], list[str]]:
    leaders: list[Leader] = []
    links_list: list[str] = []

    r = requests.get('https://api.wikimedia.org/core/v1/wikipedia/en/page/List_of_current_heads_of_state_and_government/html')

    soup = BeautifulSoup(r.text, 'html.parser')

    ts_l, links_l = table_scrape('Current_monarchs_of_sovereign_states', soup, exists)
    leaders.extend(ts_l)
    links_list.extend(links_l)

    ts_l, links_l = table_scrape('Current_heads_of_state_of_republics', soup, exists)
    leaders.extend(ts_l)
    links_list.extend(links_l)

    ts_l, links_l = table_scrape('Currents_heads_of_government', soup, exists)
    leaders.extend(ts_l)
    links_list.extend(links_l)

    # print(leaders)

    # output to json file
    with open('leaders.json', 'w') as f:
        f.write(json.dumps((leaders, links_list), indent=4))

    return leaders, links_list

# scrape(exists=[])

def supabase(re_scrape: bool = False):
    url: str = os.environ.get("PUBLIC_SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SERVICE_KEY")
    supabase: Client = create_client(url, key)

    # bulk get leader, leader_states, states
    leaders, leaders_count = supabase.table('leaders').select("*").execute()
    leader_states, leader_states_count = supabase.table('leader_states').select("*").execute()
    states, states_count = supabase.table('states').select("*").execute()

    leaders = leaders[1]
    leader_states = leader_states[1]
    states = states[1]

    states_url_set = set()
    for state in states:
        states_url_set.add(state['wikipedia_link'])

    # get all leader wikipedia links
    leader_links = set()
    for leader in leaders:
        leader_links.add(leader['wikipedia_link'])

    if re_scrape:
        scrape(exists=leader_links)
    with open('leaders.json', 'r') as f:
        leaders_to_add, leader_links_list = json.loads(f.read())

    # remove all existing leaders from leaders_to_add
    new_leaders = []
    for leader in leaders_to_add:
        if leader['wikipedia_link'] not in leader_links:
            new_leaders.append(leader)
            leader_links.add(leader['wikipedia_link'])

    states_to_insert = []
    leader_states = []

    for leader in new_leaders:
        for state in leader['states']:
            if state['wikipedia_link'] not in states_url_set:
                states_to_insert.append(state)
                states_url_set.add(state['wikipedia_link'])
            leader_states.append({
                'state_link': state['wikipedia_link'],
                'leader_link': leader['wikipedia_link']
            })
        del leader['states']

    leader_links_set = set(leader_links_list)

    # deduplicate new leaders
    # new_new_leaders = []
    # new_new_leaders_links = set()
    # for leader in new_leaders:
    #     if leader['wikipedia_link'] not in new_new_leaders_links:
    #         new_new_leaders.append(leader)
    #     new_new_leaders_links.add(leader['wikipedia_link'])
    # new_leaders = new_new_leaders

    # insert new leaders, insert new states, check if leaders are active based on links lists, insert leader_states

    # check if leader is active
    for leader in leaders:
        if leader['wikipedia_link'] not in leader_links_set:
            supabase.table('leaders').update({
                'active': False
            }).match({
                'wikipedia_link': leader['wikipedia_link']
            }).execute()

    # insert new states
    supabase.table('states').insert(states_to_insert).execute()

    # insert new leaders
    data, count = supabase.table('leaders').insert(new_leaders).execute()
    print(f'inserted {count} new leaders')

    # insert leader_states
    supabase.table('leader_states').insert(leader_states).execute()

    # insert leader_categories
    leader_categories, count = supabase.table('leader_categories').select('*').eq('category', 'current').execute()

    leader_categories = leader_categories[1]

    categories_url_set = set()

    for leader_category in leader_categories:
        categories_url_set.add(leader_category['leader_link'])

    # for every leader in wikipedia_links, insert into leader_categories
    leader_categories_to_insert = [
        {
            'leader': leader_link,
            'category': 'current'
        }
        for leader_link in leader_links_list if leader_link not in categories_url_set
    ]

    supabase.table('leader_categories').insert(leader_categories_to_insert).execute()


supabase(re_scrape=False)

