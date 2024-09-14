<script>
	import { apiUrl, getAllData } from '$lib/api.js';
	import { toImportData } from '$lib/utils.js';

	import { viewStore } from '$lib/stores.js';

	import Header from '$lib/Header.svelte';
	import Overview from '$lib/Overview.svelte';
	import ComponentsList from '$lib/ComponentsList.svelte';
	import Footer from '$lib/Footer.svelte';
	import Dummy from '$lib/Dummy.svelte';

	/** @type {import('./$types').PageData} */
	export let data;

	if (!toImportData) {
		data = getAllData();
	}

	let view = '';

	viewStore.subscribe((value) => (view = value));

	$: view;
</script>

<Header />

{#await data}
	<Dummy />
{:then data}
	<Overview
		status={data.overview.status}
		componentsCount={data.overview.components_count}
		issuesCount={data.overview.issues_count}
		componentsIssues={data.overview.components_issues}
		datetimeHuman={data.overview.datetime_human}
	/>
	<ComponentsList components={data.components} componentsData={data.componentsData} {view} />
{:catch error}
	<Dummy error={error.message} />
{/await}

<Footer />
