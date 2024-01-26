<script lang="ts">
	import 'tailwindcss/tailwind.css'
	import '../app.css'
	import Themes from './Themes.svelte'
	import HideNames from './HideNames.svelte'
	import AnimationSpeed from './AnimationSpeed.svelte'
</script>

<div class="h-screen w-screen">
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
					<li><a href="/categories/">Categories</a></li>
					<li><a href="https://github.com/AidanG1/leaders" target="_blank">Source Code</a></li>
				</ul>
			</div>
			<a class="btn btn-ghost text-2xl" href="/">🔥🥵🥺 World Leaders</a>
		</div>
		<div class="navbar-center hidden lg:flex">
			<ul class="menu menu-horizontal px-1">
				<li><a href="/">Vote</a></li>
				<li><a href="/categories/">Categories</a></li>
				<li><a href="https://github.com/AidanG1/leaders" target="_blank">Source Code</a></li>
			</ul>
		</div>
	</div>
	<div class="container">
		<slot />
	</div>
	<footer class="footer p-10 bg-neutral text-neutral-content h-fit">
		<aside>
			<img src="/hotface.png" class="w-36 h-36" alt="Hot face logo" />
			<p>🔥🥵🥺 World Leaders<br />Click the hottest one</p>
		</aside>
		<nav>
			<h6 class="footer-title">Instructions</h6>
			<p>
				Get shown 2 world leaders, click the hottest one. Contribute to science! It's that easy!
			</p>
		</nav>
		<nav>
			<Themes />
			<HideNames />
			<AnimationSpeed />
		</nav>
	</footer>
</div>
