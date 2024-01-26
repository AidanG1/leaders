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
</script>

<div class="navbar bg-base-100">
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
			<ul class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
				<li><a href="/">Vote</a></li>
				<li><a href="/leaderboard">Leaderboard</a></li>
			</ul>
		</div>
		<a class="btn btn-ghost text-2xl" href="/">🔥🥵🥺 World Leaders</a>
	</div>
	<div class="navbar-center hidden lg:flex">
		<ul class="menu menu-horizontal px-1">
			<li><a href="/">Vote</a></li>
			<li><a href="/leaderboard">Leaderboard</a></li>
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
			<ul class="dropdown-content z-[1] p-2 shadow-2xl bg-base-300 rounded-box w-52">
				<li>
					<input
						type="radio"
						name="theme-dropdown"
						class="theme-controller btn btn-sm btn-block btn-ghost justify-start"
						aria-label="Default"
						value="default"
                        on:change={() => changeTheme('default')}
					/>
				</li>
				<li>
					<input
						type="radio"
						name="theme-dropdown"
						class="theme-controller btn btn-sm btn-block btn-ghost justify-start"
						aria-label="Retro"
						value="retro"
                        on:change={() => changeTheme('retro')}
					/>
				</li>
				<li>
					<input
						type="radio"
						name="theme-dropdown"
						class="theme-controller btn btn-sm btn-block btn-ghost justify-start"
						aria-label="Cyberpunk"
						value="cyberpunk"
                        on:change={() => changeTheme('cyberpunk')}
					/>
				</li>
				<li>
					<input
						type="radio"
						name="theme-dropdown"
						class="theme-controller btn btn-sm btn-block btn-ghost justify-start"
						aria-label="Valentine"
						value="valentine"
                        on:change={() => changeTheme('valentine')}
					/>
				</li>
				<li>
					<input
						type="radio"
						name="theme-dropdown"
						class="theme-controller btn btn-sm btn-block btn-ghost justify-start"
						aria-label="Aqua"
						value="aqua"
                        on:change={() => changeTheme('aqua')}
					/>
				</li>
			</ul>
		</div>
	</div>
</div>
<div class="container px-4">
	<slot />
</div>
