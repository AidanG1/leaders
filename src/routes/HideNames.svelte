<script lang="ts">
	import { onMount } from 'svelte'
    import { chn } from '$lib/hide_names.svelte';
    
	onMount(() => {
		const stored = localStorage.getItem('hide_names')

		let stored_value = false

		// parse as boolean
		if (stored === 'true') {
			stored_value = true
		}

		// set the stored value
		chn.hide_names = stored_value

		$effect(() => {
			// Anytime the store changes, update the local storage value.
			localStorage.setItem('hide_names', chn.hide_names ? 'true' : 'false')
		})
	})
</script>

<input type="checkbox" class="toggle" bind:checked={chn.hide_names} />
