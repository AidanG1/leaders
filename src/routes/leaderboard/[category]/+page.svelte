<script lang="ts">
	let { data } = $props()
</script>

<h1>Leaderboard</h1>
<table class="table w-screen">
	<thead>
		<tr>
			<th>Image</th>
			<th>Name</th>
			<th>Wins</th>
			<th>Losses</th>
			<th>Win Rate</th>
		</tr>
	</thead>
	<tbody>
		{#each data.leaders as leader}
			<tr class="border-y-2">
				<td
					><img
						src={leader.image_url}
						alt={leader.leader_name}
						class="h-24 rounded-lg w-auto shadow-md"
						loading="lazy"
					/></td
				>
				<td class="text-xl text-primary"
					><a href="https://en.wikipedia.org/wiki/{leader.wikipedia_link}">{leader.leader_name}</a
					></td
				>
				<td>{leader.total_wins}</td>
				<td>{leader.total_losses}</td>
				<td>{(leader.win_percentage * 100).toFixed(2)}%</td>
			</tr>
		{/each}
	</tbody>
</table>
