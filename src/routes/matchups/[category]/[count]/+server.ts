import { error, json } from '@sveltejs/kit'
import { supabase } from '$lib/db'
import type { Matchup } from '$lib/types'

export async function GET({ params }) {
    const { data, error: fetchError } = await supabase
        .from('leader_categories')
        .select('leader(id, created_at, name, wikipedia_link, image_url, title), *')
        .eq('category', params.category)

    
    if (fetchError) {
        return error(500, fetchError.message)
    }
    
    if (!data) {
        return error(404, 'Not found')
    }

    // url should contain the number of matchups to return
    const matchupsString = params.count
    if (!matchupsString) {
        return error(400, 'Bad request')
    }
    const numMatchups = parseInt(matchupsString)

    const matchups: Matchup[] = []

    for (let i = 0; i < numMatchups; i++) {
        const matchup = {
            leader1: data[Math.floor(Math.random() * data.length)].leader,
            leader2: data[Math.floor(Math.random() * data.length)].leader
        }
        while (matchup.leader1 === matchup.leader2) {
            matchup.leader2 = data[Math.floor(Math.random() * data.length)].leader
        }
        matchups.push(matchup)
    }

    return json({ matchups })
}