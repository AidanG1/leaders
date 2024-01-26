<script lang="ts">
	import 'tailwindcss/tailwind.css'
	import '../app.css'

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

<div class="h-screen w-screen overflow-x-hidden">
	<div class="navbar bg-base-100 border-b-2 border-primary">
		<div class="navbar-start">
			<div class="dropdown">
				<div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
						><path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M4 6h16M4 12h8m-8 6h16"
						/></svg
					>
				</div>
				<ul
					class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
				>
					<li><a href="/">Vote</a></li>
					<li><a href="/leaderboard">Leaderboard</a></li>
					<li><a href="https://github.com/AidanG1/leaders" target="_blank">Source Code</a></li>
				</ul>
			</div>
			<a class="btn btn-ghost text-2xl" href="/">🔥🥵🥺 World Leaders</a>
		</div>
		<div class="navbar-center hidden lg:flex">
			<ul class="menu menu-horizontal px-1">
				<li><a href="/">Vote</a></li>
				<li><a href="/leaderboard">Leaderboard</a></li>
				<li><a href="https://github.com/AidanG1/leaders" target="_blank">Source Code</a></li>
			</ul>
		</div>
		<div class="navbar-end">
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
					class="dropdown-content z-[1] p-2 shadow-2xl bg-base-300 rounded-box w-52 overflow-y-scroll max-h-screen"
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
		</div>
	</div>
	<div class="container px-4">
		<slot />
	</div>
	<footer class="footer p-10 bg-neutral text-neutral-content">
		<aside>
            <img src="/hotface.png" class="w-36 h-36" alt="Hot face logo">
			<p>🔥🥵🥺 World Leaders<br />Click the hottest one</p>
		</aside>
		<nav>
			<h6 class="footer-title">Instructions</h6>
            <p>Get shown 2 world leaders, click the hottest one. Contribute to science! It's that easy!</p>
		</nav>
	</footer>
</div>
