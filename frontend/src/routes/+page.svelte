<script>
	import { getAllData } from '$lib/api.js';
	import { isBuildingSnapshot } from '$lib/utils.js';

	import { get } from 'svelte/store';
	import { viewStore } from '$lib/stores.js';

	import Header from '$lib/Header.svelte';
	import Overview from '$lib/Overview.svelte';
	import ComponentsList from '$lib/ComponentsList.svelte';
	import Footer from '$lib/Footer.svelte';
	import Dummy from '$lib/Dummy.svelte';

	/** @type {import('./$types').PageData} */
	export let data;

	if (!isBuildingSnapshot) {
		data = getAllData();
	}

	let view = '';

	viewStore.subscribe((value) => (view = value));

	$: view = get(viewStore);
</script>

<Header />

{#await data}
	<Dummy />
{:then data}
	<Overview {...data.overview} />
	<ComponentsList components={data.components} componentsData={data.componentsData} {view} />
{:catch error}
	<Dummy error={error.message} />
{/await}

<Footer />
