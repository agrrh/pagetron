<script>
	import { apiUrl } from '$lib/api.js'

	import Component from '$lib/Component.svelte';

	export let components = [];
	export let view = 'day';

	async function fetchData(name, view) {
		let response;

		response = await fetch(apiUrl + `/components/?name=${name}&view=${view}`);
		const data = await response.json();

		return data;
	}

	$: components;
</script>

<section>
	<div class="container">
		{#each components as componentName}
			{#await fetchData(componentName, view)}
				<Component name="{componentName}" dummy="true" />
			{:then data}
				<Component name={data.name} observations={data.observations} uptime={data.uptime} {view} />
			{:catch error}
				<Component name="..." dummy="true" />
			{/await}
		{/each}
	</div>
</section>
