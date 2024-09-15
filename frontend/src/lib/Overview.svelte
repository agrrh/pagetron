<script>
	export let status = false;
	export let components_count = 0;
	export let issues_count = 0;
	export let components_issues = [];
	export let datetime_human = 'Dec 01 at 00:01';

	let statusClass = '';
	let statusText = 'Unknown';

	if (status == true) {
		statusClass = 'is-success';
		statusText = 'All components online';
	} else {
		if (issues_count == components_count) {
			statusClass = 'is-danger';
			statusText = 'All components down!';
		} else {
			statusClass = 'is-warning';
			statusText = `${issues_count} component(s) unavailable`;
		}
	}
</script>

<div class="container status">
	<div class="notification has-text-centered {statusClass}">
		<p class="title">{statusText}</p>
		<p class="subtitle is-size-6">Last updated on {datetime_human} UTC</p>
	</div>
</div>

<style>
	div.status {
		margin-top: 32px;
		margin-bottom: 32px;
	}
</style>
