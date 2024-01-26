import { supabase } from '$lib/db'

export const load = async ({params}) => {
    const { data, error } = await supabase.rpc('leaderboard', {leaderboard_category: params.category})

    if (error) {
        console.log(error)
    }

    let leaders = data

    if (!leaders) leaders = []

    const category = params.category

    return {
        leaders,
        category
    }
}