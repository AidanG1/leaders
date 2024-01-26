import json, os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

presidents = [
    {
        'name': 'George Washington',
        'wikipedia_link': 'George_Washington',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg/300px-Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg',
        'title': '1st President of the United States'
    },
    {
        'name': 'John Adams',
        'wikipedia_link': 'John_Adams',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/John_Adams_A18236.jpg/300px-John_Adams_A18236.jpg',
        'title': '2nd President of the United States'
    },
    {
        'name': 'Thomas Jefferson',
        'wikipedia_link': 'Thomas_Jefferson',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Thomas_Jefferson_by_Rembrandt_Peale%2C_1800.jpg/300px-Thomas_Jefferson_by_Rembrandt_Peale%2C_1800.jpg',
        'title': '3rd President of the United States'
    },
    {
        'name': 'James Madison',
        'wikipedia_link': 'James_Madison',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/James_Madison.jpg/300px-James_Madison.jpg',
        'title': '4th President of the United States'
    },
    {
        'name': 'James Monroe',
        'wikipedia_link': 'James_Monroe',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/James_Monroe_White_House_portrait_1819.jpg/300px-James_Monroe_White_House_portrait_1819.jpg',
        'title': '5th President of the United States'
    },
    {
        'name': 'John Quincy Adams',
        'wikipedia_link': 'John_Quincy_Adams',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/John_Quincy_Adams_by_Charles_Osgood.jpg/300px-John_Quincy_Adams_by_Charles_Osgood.jpg',
        'title': '6th President of the United States'
    },
    {
        'name': 'Andrew Jackson',
        'wikipedia_link': 'Andrew_Jackson',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Andrew_jackson_head.jpg/300px-Andrew_jackson_head.jpg',
        'title': '7th President of the United States'
    },
    {
        'name': 'Martin Van Buren',
        'wikipedia_link': 'Martin_Van_Buren',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Martin_Van_Buren_circa_1837_crop.jpg/300px-Martin_Van_Buren_circa_1837_crop.jpg',
        'title': '8th President of the United States'
    },
    {
        'name': 'William Henry Harrison',
        'wikipedia_link': 'William_Henry_Harrison',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/William_Henry_Harrison_by_James_Reid_Lambdin%2C_1835_crop.jpg/300px-William_Henry_Harrison_by_James_Reid_Lambdin%2C_1835_crop.jpg',
        'title': '9th President of the United States'
    },
    {
        'name': 'John Tyler',
        'wikipedia_link': 'John_Tyler',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/John_Tyler_crop.jpg/300px-John_Tyler_crop.jpg',
        'title': '10th President of the United States'
    },
    {
        'name': 'James K. Polk',
        'wikipedia_link': 'James_K._Polk',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/JKP.jpg/300px-JKP.jpg',
        'title': '11th President of the United States'
    },
    {
        'name': 'Zachary Taylor',
        'wikipedia_link': 'Zachary_Taylor',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Zachary_Taylor_restored_and_cropped.jpg/300px-Zachary_Taylor_restored_and_cropped.jpg',
        'title': '12th President of the United States'
    },
    {
        'name': 'Millard Fillmore',
        'wikipedia_link': 'Millard_Fillmore',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Fillmore.jpg/300px-Fillmore.jpg',
        'title': '13th President of the United States'
    },
    {
        'name': 'Franklin Pierce',
        'wikipedia_link': 'Franklin_Pierce',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Mathew_Brady_-_Franklin_Pierce_-_alternate_crop_%28cropped%29.jpg/300px-Mathew_Brady_-_Franklin_Pierce_-_alternate_crop_%28cropped%29.jpg',
        'title': '14th President of the United States'
    },
    {
        'name': 'James Buchanan',
        'wikipedia_link': 'James_Buchanan',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/James_Buchanan.jpg/300px-James_Buchanan.jpg',
        'title': '15th President of the United States'
    },
    {
        'name': 'Abraham Lincoln',
        'wikipedia_link': 'Abraham_Lincoln',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg/300px-Abraham_Lincoln_O-77_matte_collodion_print.jpg',
        'title': '16th President of the United States'
    },
    {
        'name': 'Andrew Johnson',
        'wikipedia_link': 'Andrew_Johnson',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Andrew_Johnson_photo_portrait_head_and_shoulders%2C_c1870-1880-Edit1.jpg/300px-Andrew_Johnson_photo_portrait_head_and_shoulders%2C_c1870-1880-Edit1.jpg',
        'title': '17th President of the United States'
    },
    {
        'name': 'Ulysses S. Grant',
        'wikipedia_link': 'Ulysses_S._Grant',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Ulysses_S_Grant_by_Brady_c1870-restored.jpg/300px-Ulysses_S_Grant_by_Brady_c1870-restored.jpg',
        'title': '18th President of the United States'
    },
    {
        'name': 'Rutherford B. Hayes',
        'wikipedia_link': 'Rutherford_B._Hayes',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/President_Rutherford_Hayes_1870_-_1880_Restored.jpg/300px-President_Rutherford_Hayes_1870_-_1880_Restored.jpg',
        'title': '19th President of the United States'
    },
    {
        'name': 'James A. Garfield',
        'wikipedia_link': 'James_A._Garfield',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/James_Abram_Garfield%2C_photo_portrait_seated.jpg/300px-James_Abram_Garfield%2C_photo_portrait_seated.jpg',
        'title': '20th President of the United States'
    },
    {
        'name': 'Chester A. Arthur',
        'wikipedia_link': 'Chester_A._Arthur',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Chester_A._Arthur_by_Abraham_Bogardus_-_black_%26_white.jpg/300px-Chester_A._Arthur_by_Abraham_Bogardus_-_black_%26_white.jpg',
        'title': '21st President of the United States'
    },
    {
        'name': 'Grover Cleveland',
        'wikipedia_link': 'Grover_Cleveland',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Grover_Cleveland_-_NARA_-_518139_%28cropped%29.jpg/300px-Grover_Cleveland_-_NARA_-_518139_%28cropped%29.jpg',
        'title': '22nd and 24th President of the United States'
    },
    {
        'name': 'Benjamin Harrison',
        'wikipedia_link': 'Benjamin_Harrison',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Benjamin_Harrison%2C_head_and_shoulders_bw_photo%2C_1896.jpg/300px-Benjamin_Harrison%2C_head_and_shoulders_bw_photo%2C_1896.jpg',
        'title': '23rd President of the United States'
    },
    {
        'name': 'William McKinley',
        'wikipedia_link': 'William_McKinley',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Mckinley.jpg/300px-Mckinley.jpg',
        'title': '25th President of the United States'
    },
    {
        'name': 'Theodore Roosevelt',
        'wikipedia_link': 'Theodore_Roosevelt',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Theodore_Roosevelt_by_the_Pach_Bros.jpg/300px-Theodore_Roosevelt_by_the_Pach_Bros.jpg',
        'title': '26th President of the United States'
    },
    {
        'name': 'William Howard Taft',
        'wikipedia_link': 'William_Howard_Taft',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/William_Howard_Taft%2C_head-and-shoulders_portrait%2C_facing_front.jpg/300px-William_Howard_Taft%2C_head-and-shoulders_portrait%2C_facing_front.jpg',
        'title': '27th President of the United States'
    },
    {
        'name': 'Woodrow Wilson',
        'wikipedia_link': 'Woodrow_Wilson',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/President_Wilson_1919.jpg/300px-President_Wilson_1919.jpg',
        'title': '28th President of the United States'
    },
    {
        'name': 'Warren G. Harding',
        'wikipedia_link': 'Warren_G._Harding',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Warren_G_Harding-Harris_%26_Ewing.jpg/300px-Warren_G_Harding-Harris_%26_Ewing.jpg',
        'title': '29th President of the United States'
    },
    {
        'name': 'Calvin Coolidge',
        'wikipedia_link': 'Calvin_Coolidge',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Calvin_Coolidge_cph.3g10777_%28cropped%29.jpg/300px-Calvin_Coolidge_cph.3g10777_%28cropped%29.jpg',
        'title': '30th President of the United States'
    },
    {
        'name': 'Herbert Hoover',
        'wikipedia_link': 'Herbert_Hoover',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/President_Hoover_portrait.jpg/300px-President_Hoover_portrait.jpg',
        'title': '31st President of the United States'
    },
    {
        'name': 'Franklin D. Roosevelt',
        'wikipedia_link': 'Franklin_D._Roosevelt',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/FDR_1944_Color_Portrait.jpg/300px-FDR_1944_Color_Portrait.jpg',
        'title': '32nd President of the United States'
    },
    {
        'name': 'Harry S. Truman',
        'wikipedia_link': 'Harry_S._Truman',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/TRUMAN_58-766-06_%28cropped%29.jpg/300px-TRUMAN_58-766-06_%28cropped%29.jpg',
        'title': '33rd President of the United States'
    },
    {
        'name': 'Dwight D. Eisenhower',
        'wikipedia_link': 'Dwight_D._Eisenhower',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Dwight_D._Eisenhower%2C_official_photo_portrait%2C_May_29%2C_1959.jpg/300px-Dwight_D._Eisenhower%2C_official_photo_portrait%2C_May_29%2C_1959.jpg',
        'title': '34th President of the United States'
    },
    {
        'name': 'John F. Kennedy',
        'wikipedia_link': 'John_F._Kennedy',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/John_F._Kennedy%2C_White_House_color_photo_portrait.jpg/300px-John_F._Kennedy%2C_White_House_color_photo_portrait.jpg',
        'title': '35th President of the United States'
    },
    {
        'name': 'Lyndon B. Johnson',
        'wikipedia_link': 'Lyndon_B._Johnson',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/37_Lyndon_Johnson_3x4.jpg/300px-37_Lyndon_Johnson_3x4.jpg',
        'title': '36th President of the United States'
    },
    {
        'name': 'Richard Nixon',
        'wikipedia_link': 'Richard_Nixon',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Richard_Nixon_presidential_portrait_%281%29.jpg/300px-Richard_Nixon_presidential_portrait_%281%29.jpg',
        'title': '37th President of the United States'
    },
    {
        'name': 'Gerald Ford',
        'wikipedia_link': 'Gerald_Ford',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Gerald_Ford_presidential_portrait_%28cropped_3%29.jpg/300px-Gerald_Ford_presidential_portrait_%28cropped_3%29.jpg',
        'title': '38th President of the United States'
    },
    {
        'name': 'Jimmy Carter',
        'wikipedia_link': 'Jimmy_Carter',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/JimmyCarterPortrait2.jpg/300px-JimmyCarterPortrait2.jpg',
        'title': '39th President of the United States'
    },
    {
        'name': 'Ronald Reagan',
        'wikipedia_link': 'Ronald_Reagan',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/JimmyCarterPortrait2.jpg/300px-JimmyCarterPortrait2.jpg',
        'title': '40th President of the United States'
    },
    {
        'name': 'George H. W. Bush',
        'wikipedia_link': 'George_H._W._Bush',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/George_H._W._Bush_presidential_portrait_%28cropped%29.jpg/300px-George_H._W._Bush_presidential_portrait_%28cropped%29.jpg',
        'title': '41st President of the United States'
    },
    {
        'name': 'Bill Clinton',
        'wikipedia_link': 'Bill_Clinton',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Bill_Clinton.jpg/300px-Bill_Clinton.jpg',
        'title': '42nd President of the United States'
    },
    {
        'name': 'George W. Bush',
        'wikipedia_link': 'George_W._Bush',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/George-W-Bush.jpeg/300px-George-W-Bush.jpeg',
        'title': '43rd President of the United States'
    },
    {
        'name': 'Barack Obama',
        'wikipedia_link': 'Barack_Obama',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Official_portrait_of_Barack_Obama.jpg/300px-Official_portrait_of_Barack_Obama.jpg',
        'title': '44th President of the United States'
    },
    {
        'name': 'Donald Trump',
        'wikipedia_link': 'Donald_Trump',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Donald_Trump_official_portrait.jpg/300px-Donald_Trump_official_portrait.jpg',
        'title': '45th President of the United States'
    },
    {
        'wikipedia_link': 'Joe_Biden',
    }
]

# all have United_States and category presidents, active False

def supabase():
    url: str = os.environ.get("PUBLIC_SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SERVICE_KEY")
    supabase: Client = create_client(url, key)

    # bulk get leader, leader_states, states
    leaders, leaders_count = supabase.table('leaders').select("*").execute()
    leader_categories, leader_categories_count = supabase.table('leader_categories').select("*").eq('category', 'presidents').execute()

    leaders = leaders[1]
    leader_categories = leader_categories[1]

    leader_links = set()
    for leader in leaders:
        leader_links.add(leader['wikipedia_link'])

    
    leaders_to_insert = []
    for president in presidents:
        if president['wikipedia_link'] not in leader_links:
            leaders_to_insert.append(president)


    leader_categories_links = set()
    for leader_category in leader_categories:
        leader_categories_links.add(leader_category['leader'])

    leader_categories_to_insert = []
    for president in presidents:
        if president['wikipedia_link'] not in leader_categories_links:
            leader_categories_to_insert.append({
                'leader': president['wikipedia_link'],
                'category': 'presidents'
            })

    supabase.table('leaders').insert(leaders_to_insert).execute()
    supabase.table('leader_categories').insert(leader_categories_to_insert).execute()

if __name__ == '__main__':
    supabase()