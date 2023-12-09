<script>
	import { apiUrl } from '$lib/api.js'

	import { viewStore } from '$lib/stores.js';

	import Header from '$lib/Header.svelte';
	import Overview from '$lib/Overview.svelte';
	import ComponentsList from '$lib/ComponentsList.svelte';
	import Footer from '$lib/Footer.svelte';
	import Dummy from '$lib/Dummy.svelte';

	async function fetchData() {
		let response;

		response = await fetch(apiUrl + `/overview/`);
		const overview = await response.json();

		response = await fetch(apiUrl + `/components/`);
		const components = await response.json();

		return { overview, components };
	}

	let view = '';

	viewStore.subscribe((value) => (view = value));

	$: view;
</script>

<Header />

{#await fetchData()}
	<Dummy />
{:then data}
	<Overview
		status={data.overview.status}
		componentsCount={data.overview.components_count}
		issuesCount={data.overview.issues_count}
		componentsIssues={data.overview.components_issues}
		datetimeHuman={data.overview.datetime_human}
	/>
	<ComponentsList components={data.components} {view} />
{:catch error}
	<Dummy error={error.message} />
{/await}

<Footer />
