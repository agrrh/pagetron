<script>
	import Component from '$lib/Component.svelte';

	let resources = [1, 2];
</script>

<section>
	<div class="container">
		{#each resources as resource}
			<Component />
		{/each}
	</div>
</section>
