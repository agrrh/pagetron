<script>
	import Component from '$lib/Component.svelte';

	export let components = [];
	export let view = 'day';

	async function fetchData(name, view) {
		let response;

		response = await fetch(`http://127.0.0.1:3000/components/?name=${name}&view=${view}`);
		const data = await response.json();

		return data;
	}

	$: components;
</script>

<section>
	<div class="container">
		{#each components as componentName}
			{#await fetchData(componentName, view)}
				<Component name="..." dummy="true" />
			{:then data}
				<Component name={data.name} observations={data.observations} uptime={data.uptime} {view} />
			{:catch error}
				<Component name="..." dummy="true" />
			{/await}
		{/each}
	</div>
</section>
