<script lang="ts">
	import type { Database } from '$lib/supabase'
	import { fly, slide } from 'svelte/transition'
	import { createEventDispatcher, tick } from 'svelte'
	import { chn } from '$lib/hide_names.svelte'


	let {
		leader,
		animation_duration = 2000,
		loser = false
	} = $props<{
		leader: Database['public']['Tables']['leaders']['Row']
		animation_duration: number
		loser: boolean
	}>()

	let show_image = $state(false)

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
					{ transform: 'scale(1)', backgroundColor: 'initial' },
					{ transform: 'scale(0.5) rotate(360deg)', backgroundColor: 'red' },
					{ transform: 'scale(0) rotate(1200deg)', backgroundColor: 'initial' }
				],
				{
					duration: animation_duration + 500,
					easing: 'ease-in-out'
				}
			)
		}
	})

	$effect.pre(() => {
		show_image = false

		tick().then(() => {
			show_image = true
		})
	})
</script>

<div class="p-2" in:fly out:slide bind:this={div}>
	<button on:click={() => submit_vote(leader)} class="flex justify-center w-full max-w-1/2">
		{#if show_image}
			<img
				src={leader.image_url}
				alt={leader.name}
				class="md:h-96 rounded-lg border-primary border-2 hover:scale-110 transition-transform shadow-md"
			/>
		{/if}
	</button>
	{#if !chn.hide_names}
		<h2 class="text-center mt-4">
			<a href="https://en.wikipedia.org/wiki/{leader.wikipedia_link}" class="text-primary text-2xl">
				{leader.name} <span class="text-secondary">{leader.title}</span>
			</a>
		</h2>
	{/if}
</div>
