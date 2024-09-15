<script>
	import humanizeDuration from 'humanize-duration';

	import { get } from 'svelte/store';
	import { viewStore } from '$lib/stores.js';

	import Tick from '$lib/Tick.svelte';

	export let dummy = false;
	export let view = 'quarter';

	export let name = 'changeme';
	export let uptime = 0.0;
	export let observations = [];
	export let tickCapacitySeconds = 60;

	let uptimeStateClasses = '';

	if (dummy) {
		observations = Array.from({ length: 90 }, () => -1.0);
	}

	function urlSplit(url) {
		if (url == null || url.length < 5) {
			return ['file://', '/dev/null'];
		}

		let urlObj = new URL(url);

		let proto = urlObj.protocol + '//';
		let hostAndPath = urlObj.hostname;

		if (urlObj.pathname.length > 1) {
			hostAndPath += urlObj.pathname;
		}

		return [proto, hostAndPath];
	}

	function addProto(url) {
		return url.startsWith('http') ? url : 'http://' + url;
	}

	function getUptimeStateClasses(uptime) {
		let thresholds = [0.99, 0.95];

		if (dummy) {
			uptimeStateClasses = 'has-text-grey';
		} else if (uptime > thresholds[0]) {
			uptimeStateClasses = 'has-text-success';
		} else if (uptime > thresholds[1]) {
			uptimeStateClasses = 'has-text-warning-dark';
		} else {
			uptimeStateClasses = 'has-text-danger-dark';
		}

		return uptimeStateClasses;
	}

	function getTimelineStart(view) {
		let timelineStart = '';

		switch (view) {
			case 'hours':
				timelineStart = '6 hours';
				break;
			case 'quarter':
				timelineStart = '90 days';
				break;
			case 'year':
				timelineStart = 'year';
				break;
		}

		return timelineStart;
	}

	function getTickCapacitySeconds(view) {
		let tickCapacitySeconds = 60;

		switch (view) {
			case 'hours':
				tickCapacitySeconds = 60 * 5;
				break;
			case 'quarter':
				tickCapacitySeconds = 60 * 60 * 24;
				break;
			case 'year':
				tickCapacitySeconds = 60 * 60 * 24 * 7;
				break;
		}

		return tickCapacitySeconds;
	}

	viewStore.subscribe((value) => (view = value));

	$: view = get(viewStore);
	$: uptimeStateClasses = getUptimeStateClasses(uptime);
	$: timelineStart = getTimelineStart(view);
	$: tickCapacitySeconds = getTickCapacitySeconds(view);
	$: tickCapacityHuman = humanizeDuration(tickCapacitySeconds * 1000, {
		maxDecimalPoints: 1,
		units: ['w', 'd', 'h', 'm', 's']
	});
	$: uptimeHuman = (uptime * 100.0).toFixed(2);
</script>

<div class="box">
	<div class="header columns is-mobile">
		<div class="column is-3">
			<p class="is-size-5 has-text-weight-bold">
				<a class="has-text-link-dark" href={addProto(name)} target="_blank">{name}</a>
			</p>
		</div>
		<div class="column has-text-right">
			<p class="is-text-bold is-family-code {uptimeStateClasses}">
				{uptimeHuman}%
			</p>
		</div>
	</div>

	<div class="body">
		{#if dummy}
			<progress class="progress is-small is-gray mt-2 mb-1" max="100">0%</progress>
		{:else}
			{#each observations as tick}
				<Tick id={tick[0]} uptime={tick[1]} capacity={tickCapacitySeconds} />
			{/each}
		{/if}
	</div>

	<div class="info columns is-mobile has-text-grey is-size-7">
		<div class="column is-3">{timelineStart} ago</div>
		<div class="column has-text-centered">per {tickCapacityHuman}</div>
		<div class="column is-3 has-text-right">Now</div>
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
