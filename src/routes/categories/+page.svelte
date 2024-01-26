<script lang="ts">
	let { data } = $props()
</script>

<h1>Categories</h1>
<div class="grid grid-cols-3 grid-flow-row-dense auto-rows-max gap-2 p-2">
	{#each data.categories as c}
		<div class="card bg-base-100 shadow-xl image-full">
			<figure>
				<img src={c.image_url} alt={c.name} />
			</figure>
			<div class="card-body">
				<h2 class="btn btn-primary text-xl h-fit"><a href="/vote/{c.slug}/">Vote on {c.name}</a></h2>
				<h3 class="btn btn-secondary text-xl h-fit"><a href="/leaderboard/{c.slug}/">Leaderboard for {c.name}</a></h3>
				<div class="card-actions justify-end">
					<a href="https://en.wikipedia.org/wiki/{c.wikipedia_link}" class="btn btn-primary">
						Wikipedia
					</a>
				</div>
			</div>
		</div>
	{/each}
</div>
