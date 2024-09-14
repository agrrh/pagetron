<script>
	import Component from '$lib/Component.svelte';

	/** @type {import('./$types').PageData} */
	export let components = [];
	export let componentsData = {};
	export let view = 'day';

	$: components;
</script>

<section>
	<div class="container">
		{#each components as c}
			{#await c}
				<Component name={c} dummy="true" />
			{:then c}
				<Component
					name={componentsData[c][view].name}
					observations={componentsData[c][view].observations}
					uptime={componentsData[c][view].uptime}
					{view}
				/>
			{:catch error}
				<Component name="..." dummy="true" />
			{/await}
		{/each}
	</div>
</section>
