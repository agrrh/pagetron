<script>
	import Timeline from '$lib/Timeline.svelte';

	let resources = [1, 2];
</script>

<section>
	<div class="container">
		{#each resources as resource}
			<Timeline />
		{/each}
	</div>
</section>
