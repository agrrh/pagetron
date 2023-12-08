<script>
	import { viewStore } from '$lib/stores.js';

	let curViewName = '';
	let curViewIconClass = '';

	let isActiveHours = "";
	let isActiveQuarter = "";
	let isActiveYear = "";

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

	$: curViewIconClass = views.filter((x) => x.name == view)[0]['icon'];
	$: viewText = views.filter((x) => x.name == view)[0]['text'];

	$: isActiveHours = view == 'hours' ? "" : "has-text-grey";
	$: isActiveQuarter = view == 'quarter' ? "" : "has-text-grey";
	$: isActiveYear = view == 'year' ? "" : "has-text-grey";
</script>

<div class="navbar-item">
	<a id="viewSelector" class="button is-dark" on:click={nextView}>
		<span class="fa fa-clock {isActiveHours}"></span>
		<span class="fa fa-calendar-days mr-3 ml-3 {isActiveQuarter}"></span>
		<span class="fa fa-earth-asia {isActiveYear}"></span>
	</a>
</div>
