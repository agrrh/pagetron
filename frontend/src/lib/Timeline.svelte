<script>
	let data = [];

	data = Array.from(Array(90).keys());
</script>

<div class="box">
	<div class="header columns">
		<div class="column is-1">
			<p class="is-size-5">Component</p>
		</div>
		<div class="column"></div>
		<div class="column is-1 has-text-right">
			<p class="is-text-bold is-family-code has-text-success">99.999%</p>
		</div>
	</div>

	<div class="body">
		{#each data as cell}
			<div class="cell"></div>
		{/each}
	</div>

	<div class="info columns has-text-grey">
		<div class="column is-1">90 days ago</div>
		<div class="column"></div>
		<div class="column is-1 has-text-right">Today</div>
	</div>
</div>

<style>
	div.box div.columns {
		margin-bottom: 0px;
		padding-bottom: 0px;
	}

	div.box {
		margin-bottom: 12px;
		padding: 20px 20px 12px 20px;
	}

	div.box div.header div.column {
		margin: 0px 6px;
		padding: 0px 6px;
	}

	div.box div.info div.column {
		margin: 12px 6px 0px 6px;
		padding: 0px 6px;
	}

	div.header {
	}

	div.body {
		display: flex;
	}

	div.info {
		font-family: 'Quicksand', sans-serif;
		font-weight: lighter;
	}

	div.cell {
		display: block;
		margin-right: 1px;
		background-color: #48c78e;
		width: 1.1%;
		height: 24px;
	}
</style>
