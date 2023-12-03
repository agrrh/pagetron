<script>
	import Header from '$lib/Header.svelte';
	import Overview from '$lib/Overview.svelte';
	import ComponentsList from '$lib/ComponentsList.svelte';
	import Footer from '$lib/Footer.svelte';
	import Dummy from '$lib/Dummy.svelte';

	async function fetchData() {
		let response;

		response = await fetch(`http://127.0.0.1:3000/overview/`);
		const overview = await response.json();

		response = await fetch(`http://127.0.0.1:3000/components/`);
		const components = await response.json();

		return {overview, components};
	}
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
	<ComponentsList
		components={data.components}
		view="week"
	/>
{/await}

<Footer />
