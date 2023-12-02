<script>
	import Tick from '$lib/Tick.svelte';

	export let name = "changeme";
	export let thresholds = [0.990, 0.950]
	export let uptime = Math.random() * 1.00;

	let uptimes = [];
	let uptimeStateClasses = "";

	if (uptime > thresholds[0]) {
		uptimeStateClasses = "has-text-success";
	} else if (uptime > thresholds[1]) {
		uptimeStateClasses = "has-text-warning-dark";
	} else {
		uptimeStateClasses = "has-text-danger-dark";
	}

	let uptimeHuman = (uptime * 100.0).toFixed(2);

	// Generate randoms for now
	uptimes = Array.from(
		{length: 90},
		() => Math.round(
			(
				1.00
				-
				(Math.random() * 0.02)
			) * 1000.0
		) / 1000.0
	);
</script>

<div class="box">
	<div class="header columns">
		<div class="column is-4">
			<p class="is-size-5 has-text-weight-bold">{name}</p>
		</div>
		<div class="column"></div>
		<div class="column is-1 has-text-right">
			<p class="is-text-bold is-family-code {uptimeStateClasses}">{uptimeHuman}%</p>
		</div>
	</div>

	<div class="body">
		{#each uptimes as uptime, i}
			<Tick uptime={uptime} id="{i+1}.01" />
		{/each}
	</div>

	<div class="info columns has-text-grey is-size-7">
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
</style>
