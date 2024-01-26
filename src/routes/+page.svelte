<script lang="ts">
	import type { Leader, Matchup } from '$lib/types'
	import { onMount } from 'svelte'
	import { supabase } from '$lib/db'
	import LeaderVote from './LeaderVote.svelte'

	let matchups: Matchup[] = $state([])

	onMount(async () => {
		const res = await fetch('/matchups/10')
		matchups = await res.json().then((data) => data.matchups)
	})

	const animation_duration = 2000

	let is_voting = false

	let loser: Leader | null = $state(null)

	const submit_vote = async (winner: Leader) => {
		if (is_voting) return

		loser =
			matchups[0][leaders[0]].id === winner.id ? matchups[0][leaders[1]] : matchups[0][leaders[0]]

		is_voting = true
		const { data, error } = await supabase
			.from('votes')
			.insert([{ winner: winner.id, loser: loser.id }])
		if (error) {
			console.log(error)
		}

		console.log(data)

		setTimeout(async () => {
			matchups.shift()

			if (matchups.length === 0) {
				const res = await fetch('/matchups/10')
				matchups = await res.json().then((data) => data.matchups)
			}

			is_voting = false
		}, animation_duration)
	}

	const leaders: ('leader1' | 'leader2')[] = ['leader1', 'leader2']
</script>

<div class="grid md:grid-cols-2 justify-center content-center">
	{#if matchups.length === 0}
		<h1>Loading...</h1>
	{:else}
		<div class="border-r-2 border-primary">
			<LeaderVote
				on:submit_vote={(e) => submit_vote(e.detail.winner)}
				leader={matchups[0][leaders[0]]}
				{animation_duration}
				loser={loser?.id === matchups[0][leaders[0]].id}
			/>
		</div>
		<div class="border-l-2 border-primary">
		<LeaderVote
			on:submit_vote={(e) => submit_vote(e.detail.winner)}
			leader={matchups[0][leaders[1]]}
			{animation_duration}
			loser={loser?.id === matchups[0][leaders[1]].id}
		/>
        </div>
	{/if}
</div>
