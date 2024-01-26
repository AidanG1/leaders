<script lang="ts">
    import { supabase } from '$lib/db'

    async function get_leaderboard() {
        const { data, error } = await supabase.rpc('leaderboard')

        if (error) {
            console.log(error)
        }

        console.log(data)

        if (!data) return []

        return data
    }
</script>

<h1>Leaderboard</h1>
{#await get_leaderboard()}

    <h1>Loading...</h1>
    
{:then leaders}
    <table class="table w-screen">
        <thead>
            <tr>
                <th>Image</th>
                <th>Name</th>
                <th>Wins</th>
                <th>Losses</th>
                <th>Win Rate</th>
            </tr>
        </thead>
        <tbody>
            {#each leaders as leader}
                <tr class="border-y-2">
                    <td><img src={leader.image_url} alt={leader.leader_name} class="h-24 rounded-lg w-auto shadow-md" loading="lazy"/></td>
                    <td class="text-xl text-primary"><a href="https://en.wikipedia.org/wiki/{leader.wikipedia_link}">{leader.leader_name}</a></td>
                    <td>{leader.total_wins}</td>
                    <td>{leader.total_losses}</td>
                    <td>{(leader.win_percentage * 100).toFixed(2)}%</td>
                </tr>
            {/each}
        </tbody>
    </table>
{/await}