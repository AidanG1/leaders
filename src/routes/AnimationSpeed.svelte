<script lang="ts">
	import { onMount } from 'svelte'
	import { as } from '$lib/stores.svelte'

	onMount(() => {
		const stored = localStorage.getItem('animation_speed')

        let stored_value = 2000

        // parse as number
        if (stored) {
            stored_value = parseInt(stored)
        }

        // set the stored value
        as.speed = stored_value

		$effect(() => {
			localStorage.setItem('animation_speed', as.speed.toString())
		})
	})
</script>

<input
	type="range"
	min={as.get_min()}
	max={as.get_max()}
	bind:value={as.speed}
	class="range range-primary"
/>
