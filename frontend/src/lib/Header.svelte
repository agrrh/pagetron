<script>
	import ButtonGitHub from '$lib/header/ButtonGitHub.svelte';

	function toggleMenu() {
		var burger = document.querySelector('.navbar-burger');
		var menu = document.querySelector('#' + burger.dataset.target);
		burger.addEventListener('click', function () {
			burger.classList.toggle('is-active');
			menu.classList.toggle('is-active');
		});
	}
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
			<div class="navbar-start">
				<!-- <ButtonGitHub /> -->
			</div>

			<div class="navbar-end">
				<div class="navbar-item">
					<div class="dropdown is-right is-hoverable">
						<div class="dropdown-trigger">
							<button class="button is-white is-outlined" aria-haspopup="true" aria-controls="get-updates-menu">
								<span class="icon is-small">
									<i class="fas fa-bell" aria-hidden="true"></i>
								</span>
								<span>Get Updates</span>
								<span class="icon is-small">
									<i class="fas fa-angle-down" aria-hidden="true"></i>
								</span>
							</button>
						</div>
						<div class="dropdown-menu" id="get-updates-menu" role="menu">
							<div class="dropdown-content">
								<a href="/status" class="dropdown-item">
									API /status
								</a>
								<a href="/rss" class="dropdown-item">
									RSS Feed
								</a>
							</div>
						</div>
					</div>
				</div>
				<ButtonGitHub />
			</div>
		</div>
	</div>
</nav>
