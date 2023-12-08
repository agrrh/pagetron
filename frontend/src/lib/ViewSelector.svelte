<script>
	import { viewStore } from '$lib/stores.js';

	export let view = '';

	const views = [
		{ name: 'hours', icon: 'fa-clock' },
		{ name: 'quarter', icon: 'fa-calendar-days' },
		{ name: 'year', icon: 'fa-earth-asia' }
	];

	function capitalize(string) {
		return string.charAt(0).toUpperCase() + string.slice(1);
	}

	function setView(e) {
		let view = e.target.getAttribute('pagetron-data');
		if (view != null) {
			viewStore.set(view);
		}
	}

	viewStore.subscribe((value) => (view = value));
</script>

<div class="container block">
	<nav class="pagination is-centered" role="navigation" aria-label="pagination">
		<ul class="pagination-list">
			{#each views as { name, icon }, i}
				<li>
					<a
						class="
            pagination-link
            {name == view ? 'is-current' : ''}
          "
						aria-label="Goto {name} view"
						pagetron-data={name}
						on:click={setView}
					>
						<i class="fa {icon}"></i>
						&nbsp; {capitalize(name)}
					</a>
				</li>
			{/each}
		</ul>
	</nav>
</div>

<style>
	ul.pagination-list a.is-current {
		color: #0a0a0a;
		background-color: #ffffff;
		border-color: #7a7a7a;
	}
</style>
