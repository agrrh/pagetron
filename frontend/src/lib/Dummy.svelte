<script>
	export let error = null;
</script>

<section class="container hero is-large">
	<div class="hero-body">
		{#if error == null}
			<p class="title has-text-centered has-text-grey">
				<i class="fa fa-spinner fa-pulse is-size-1"></i>
			</p>
		{:else}
			<article class="message is-danger">
				<div class="message-header">
					<p>Error</p>
				</div>
				<div class="message-body">
					{error}
				</div>
			</article>
		{/if}
	</div>
</section>
