import { error, json } from '@sveltejs/kit'
import { supabase } from '$lib/db'
import type { Matchup } from '$lib/types'

export async function GET({ params }) {
    const { data, error: fetchError } = await supabase
        .from('leaders')
        .select()

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
            leader1: data[Math.floor(Math.random() * data.length)],
            leader2: data[Math.floor(Math.random() * data.length)]
        }
        matchups.push(matchup)
    }

    return json({ matchups })
}