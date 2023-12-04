<script>
	import { viewStore } from '$lib/stores.js';
	import { get } from 'svelte/store';

	function toggleMenu() {
		var burger = document.querySelector('.navbar-burger');
		var menu = document.querySelector('#' + burger.dataset.target);
		burger.addEventListener('click', function () {
			burger.classList.toggle('is-active');
			menu.classList.toggle('is-active');
		});
	}

	function nextView() {
		let i = 0;
		let viewsList = ['day', 'week', 'month', 'quarter', 'year'];

		let currentView = get(viewStore);

		i = viewsList.indexOf(currentView) + 1;

		if (i >= viewsList.length) {
			i = 0;
		}

		viewStore.set(viewsList[i]);
	}

	let view = '';

	viewStore.subscribe((value) => (view = value));

	$: view;
</script>

<nav class="navbar is-black" role="navigation" aria-label="main navigation">
	<div class="container">
		<div class="navbar-brand">
			<a class="navbar-item is-size-4" href="/">
				<span class="fa fa-file-lines"></span>
				&nbsp; Pagetron
			</a>

			<a
				role="button"
				class="navbar-burger"
				aria-label="menu"
				aria-expanded="false"
				data-target="navMenu"
				on:click={toggleMenu()}
			>
				<span aria-hidden="true"></span>
				<span aria-hidden="true"></span>
				<span aria-hidden="true"></span>
			</a>
		</div>

		<div id="navMenu" class="navbar-menu has-background-black">
			<div class="navbar-start"></div>

			<div class="navbar-end">
				<div class="navbar-item">
					<a class="button is-white is-outlined" on:click={nextView}>
						<span class="fa fa-eye"></span>
						<span class="">
							&nbsp; View: {view}
						</span>
					</a>
				</div>
			</div>
		</div>
	</div>
</nav>
