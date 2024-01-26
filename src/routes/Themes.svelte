<script lang="ts">
	import { onMount } from 'svelte'

	onMount(() => {
		const theme = localStorage.getItem('theme') || 'default'

		document.documentElement.classList.add(`theme-${theme}`)
	})

	function changeTheme(theme: string) {
		localStorage.setItem('theme', theme)
	}

	const themes = [
		'light',
		'dark',
		'cupcake',
		'bumblebee',
		'emerald',
		'corporate',
		'synthwave',
		'retro',
		'cyberpunk',
		'valentine',
		'halloween',
		'garden',
		'forest',
		'aqua',
		'lofi',
		'pastel',
		'fantasy',
		'wireframe',
		'black',
		'luxury',
		'dracula',
		'cmyk',
		'autumn',
		'business',
		'acid',
		'lemonade',
		'night',
		'coffee',
		'winter',
		'dim',
		'nord',
		'sunset'
	]
</script>

<div class="dropdown">
	<div tabindex="0" role="button" class="btn m-1 mr-2">
		Theme
		<svg
			width="16px"
			height="16px"
			class="h-2 w-2 fill-current opacity-60 inline-block"
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 2048 2048"
		>
			<path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path>
		</svg>
	</div>
	<ul
		class="dropdown-content z-[1] p-2 shadow-2xl bg-base-300 rounded-box w-52 overflow-y-scroll max-h-40 text-base-content"
	>
		{#each themes as theme}
			<li>
				<input
					type="radio"
					name="theme-dropdown"
					class="theme-controller btn btn-sm btn-block btn-ghost justify-start"
					aria-label={theme}
					value={theme}
					on:change={() => changeTheme(theme)}
				/>
			</li>
		{/each}
	</ul>
</div>
