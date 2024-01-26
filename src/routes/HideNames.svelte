<script lang="ts">
	import { onMount } from 'svelte'
	import { chn } from '$lib/stores.svelte'

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

<div class="form-control">
	<label class="label cursor-pointer">
		<span class="label-text mr-2">Hide Names</span>
		<input type="checkbox" class="toggle" bind:checked={chn.hide_names} />
	</label>
</div>
