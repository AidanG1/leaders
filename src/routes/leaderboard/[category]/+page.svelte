<script lang="ts">
	let { data } = $props()
</script>

<h1>Leaderboard</h1>
<a class="btn btn-primary w-full my-2" href="/vote/{data.category}">
	<h3 class="w-full text-center">Vote!</h3>
</a>
<table class="table w-screen">
	<thead>
		<tr>
			<th>Rank</th>
			<th>Image</th>
			<th>Name</th>
			<th>Wins</th>
			<th>Losses</th>
			<th>Win Rate</th>
		</tr>
	</thead>
	<tbody>
		{#each data.leaders as leader, i}
			<tr class="border-y-2">
				<td>{i + 1}</td>
				<td>
					<img
						src={leader.image_url}
						alt={leader.leader_name}
						class="h-24 rounded-lg w-auto shadow-md"
						loading="lazy"
					/>
				</td>
				<td class="text-xl text-primary"
					><a href="https://en.wikipedia.org/wiki/{leader.wikipedia_link}" target="_blank"
						>{leader.leader_name}</a
					></td
				>
				<td>{leader.total_wins}</td>
				<td>{leader.total_losses}</td>
				<td>{(leader.win_percentage * 100).toFixed(2)}%</td>
			</tr>
		{/each}
	</tbody>
</table>
