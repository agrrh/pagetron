<script>
	import Header from '$lib/Header.svelte';
	import Overview from '$lib/Overview.svelte';
	import ComponentsList from '$lib/ComponentsList.svelte';
	import Footer from '$lib/Footer.svelte';
	import Dummy from '$lib/Dummy.svelte';

	async function overview() {
		const response = await fetch(`http://127.0.0.1:3000/overview/`);
		const overview = await response.json();
		return overview;
	}
</script>

<Header />

{#await overview()}
	<Dummy />
{:then overview}
	<Overview
		status={overview.status}
		componentsCount={overview.components_count}
		issuesCount={overview.issues_count}
		componentsIssues={overview.components_issues}
		datetimeHuman={overview.datetime_human}
	/>
	<ComponentsList />
{/await}

<Footer />
