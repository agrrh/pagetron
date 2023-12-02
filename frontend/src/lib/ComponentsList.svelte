<script>
	import Component from '$lib/Component.svelte';

	let components = [
		"foo",
		"bar",
		"baz",
		"another-foo",
		"another-bar",
		"another-baz",
	];
</script>

<section>
	<div class="container">
		{#each components as component}
			<Component name="{component}" />
		{/each}
	</div>
</section>
