<script>
	import Component from '$lib/Component.svelte';

	let components = [
		"foo",
		"bar",
	];
</script>

<section>
	<div class="container">
		{#each components as component}
			<Component name="{component}" />
		{/each}
	</div>
</section>
