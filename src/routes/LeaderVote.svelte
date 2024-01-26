<script lang="ts">
	import type { Database } from '$lib/supabase'
	import { fly, slide } from 'svelte/transition'
	import { createEventDispatcher, tick } from 'svelte'

	let {
		leader,
		animation_duration = 2000,
		loser = false
	} = $props<{
		leader: Database['public']['Tables']['leaders']['Row']
		animation_duration: number
		loser: boolean
	}>()

	const dispatch = createEventDispatcher()

	function submit_vote(winner: Database['public']['Tables']['leaders']['Row']) {
		dispatch('submit_vote', { winner })

		div.animate(
			[
				{ transform: 'translateX(0) scale(1)', backgroundColor: 'initial' },
				{ transform: 'translateX(-100%) scale(1.5)', backgroundColor: 'green' },
				{ transform: 'translateX(0) scale(1)', backgroundColor: 'initial' },
				{ transform: 'translateX(100%) scale(1.5)', backgroundColor: 'green' },
				{ transform: 'translateX(0) scale(1)', backgroundColor: 'initial' }
			],
			{
				duration: animation_duration,
				easing: 'ease-in-out'
			}
		)
	}

	let div: HTMLDivElement

	$effect(() => {
		console.log(loser)
		if (loser) {
			div.animate(
				[
					{ transform: 'translateX(0) scale(1)', backgroundColor: 'initial' },
					{ transform: 'translateX(100%) scale(0.5)', backgroundColor: 'red' },
					{ transform: 'translateX(0) scale(1)', backgroundColor: 'initial' },
					{ transform: 'translateX(-100%) scale(0.5)', backgroundColor: 'red' },
					{ transform: 'translateX(0) scale(1)', backgroundColor: 'initial' }
				],
				{
					duration: animation_duration,
					easing: 'ease-in-out'
				}
			)
		}
	})
</script>

<div class="p-2 h-screen flex justify-center flex-col" in:fly out:slide bind:this={div}>
	<button on:click={() => submit_vote(leader)} class="flex justify-center">
		<img
			src={leader.image_url}
			alt={leader.name}
			class="h-96 rounded-lg border-primary border-2 hover:scale-110 transition-transform shadow-md"
		/>
	</button>
	<h2 class="text-center mt-4">
		<a href="https://en.wikipedia.org/wiki/{leader.wikipedia_link}" class="text-primary text-3xl">
			{leader.name} <span class="text-secondary">{leader.title}</span>
		</a>
	</h2>
</div>
