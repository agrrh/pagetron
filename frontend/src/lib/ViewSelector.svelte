<script>
	import { viewStore } from '$lib/stores.js';

	let view = '';
	let views = [
		{ name: 'year', icon: 'fa fa-earth-asia' },
		{ name: 'quarter', icon: 'fa fa-calendar-days' },
		{ name: 'hours', icon: 'fa fa-clock' }
	];

	function cycleViews(e) {
		if (view != null) {
			viewStore.set(views[2]['name']);
		}

		views = [views[1], views[2], views[0]];
	}

	viewStore.subscribe((value) => (view = value));

	$: views;
</script>

<div class="navbar-item">
	<a id="viewSelector" class="button is-dark" on:click={cycleViews}>
		<span class="{views[0]['icon']} has-text-grey"></span>
		<span class="{views[1]['icon']} mr-3 ml-3 is-size-5"></span>
		<span class="{views[2]['icon']} has-text-grey"></span>
	</a>
</div>
