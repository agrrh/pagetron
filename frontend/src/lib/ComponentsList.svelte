<script>
	import Component from '$lib/Component.svelte';

	import { get } from 'svelte/store';
	import { viewStore } from '$lib/stores.js';

	export let components = [];
	export let componentsData = {};
	export let view = 'day';

	function getDataForView(c, v) {
		return componentsData[c][v];
	}

	viewStore.subscribe((value) => (view = value));

	$: view = get(viewStore);
</script>

<section>
	<div class="container">
		{#each components as c}
			<Component {view} {...getDataForView(c, view)} />
		{/each}
	</div>
</section>
