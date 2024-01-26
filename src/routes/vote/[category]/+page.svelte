<script lang="ts">
	import type { Leader, Matchup } from '$lib/types'
	import { onMount } from 'svelte'
	import { supabase } from '$lib/db'
	import LeaderVote from '../../LeaderVote.svelte'
	import { as } from '$lib/stores.svelte'

	let { data } = $props()

	let matchups: Matchup[] = $state([])

	onMount(async () => {
		console.log(data)
		const res = await fetch(`/matchups/${data.category}/10`)
		matchups = await res.json().then((j) => j.matchups)
		console.log(matchups)
	})

	let is_voting = false

	let loser: Leader | null = $state(null)

	const submit_vote = async (winner: Leader) => {
		if (is_voting) return

		loser =
			matchups[0][leaders[0]].id === winner.id ? matchups[0][leaders[1]] : matchups[0][leaders[0]]

		is_voting = true
		const { data: votesData, error } = await supabase
			.from('votes')
			.insert([{ winner: winner.id, loser: loser.id, category: data.category }])
		if (error) {
			console.log(error)
		}

		setTimeout(async () => {
			matchups.shift()

			if (matchups.length === 0) {
				const res = await fetch(`/matchups/${data.category}/10`)
				matchups = await res.json().then((j) => j.matchups)
			}

			is_voting = false
		}, as.speed)
	}

	const leaders: ('leader1' | 'leader2')[] = ['leader1', 'leader2']
</script>

<div class="grid grid-cols-2 h-full justify-items-center w-screen overflow-x-hidden">
	{#if matchups.length === 0}
		<h1>Loading...</h1>
	{:else}
		<div class="border-r-2 border-primary w-full">
			<LeaderVote
				on:submit_vote={(e) => submit_vote(e.detail.winner)}
				leader={matchups[0][leaders[0]]}
				animation_duration={as.speed}
				loser={loser?.id === matchups[0][leaders[0]].id}
			/>
		</div>
		<div class="border-l-2 border-primary w-full">
			<LeaderVote
				on:submit_vote={(e) => submit_vote(e.detail.winner)}
				leader={matchups[0][leaders[1]]}
				animation_duration={as.speed}
				loser={loser?.id === matchups[0][leaders[1]].id}
			/>
		</div>
	{/if}
</div>
