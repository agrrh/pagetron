<script>
	import { viewStore } from '$lib/stores.js';

	let curViewName = '';
	let curViewIconClass = '';

	const views = [
		{ name: 'hours', icon: 'fa fa-clock' },
		{ name: 'quarter', icon: 'fa fa-calendar-days' },
		{ name: 'year', icon: 'fa fa-earth-asia' }
	];

	function nextView(e) {
		let viewsList = views.map((x) => x.name);
		let i = viewsList.indexOf(view) + 1;

		if (i >= views.length) {
			i = 0;
		}

		if (view != null) {
			viewStore.set(viewsList[i]);
		}
	}

	let view = '';

	viewStore.subscribe((value) => (view = value));

	$: view;
	$: curViewIconClass = views.filter((x) => x.name == view)[0]['icon'];
</script>

<div class="navbar-item">
	<a id="viewSelector" class="button is-dark has-text-left" on:click={nextView}>
		<span class={curViewIconClass}></span>
		<span class="is-capitalized"> &nbsp; {view} </span>
	</a>
</div>

<style>
	a#viewSelector {
		width: 120px;
	}
</style>
