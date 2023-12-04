<script>
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
			<div class="navbar-start"></div>

			<div class="navbar-end">
				<div class="navbar-item">
					<a
						class="button is-white is-outlined"
						href="https://github.com/agrrh/pagetron"
						target="_blank"
					>
						<span class="fab fa-github"></span>
						<span class=""> &nbsp; GitHub </span>
					</a>
				</div>
			</div>
		</div>
	</div>
</nav>
