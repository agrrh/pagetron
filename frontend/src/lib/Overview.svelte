<script>
export let status = false;
export let componentsCount = 0;
export let issuesCount = 0;
export let componentsIssues = [];
export let datetimeHuman = 'Dec 01 at 00:01';

let statusClass = '';
let statusText = 'Unknown';

if (status == true) {
	statusClass = 'is-success';
	statusText = 'All components online';
} else {
	if (issuesCount == componentsCount) {
		statusClass = 'is-danger';
		statusText = 'All components down!'
	} else {
		statusClass = 'is-warning';
		statusText = `Facing issues on ${issuesCount} component(s)`
	}
}

</script>

<div class="container status">
	<div class="notification has-text-centered {statusClass}">
		<p class="title">{statusText}</p>
		<p class="subtitle">Last updated on {datetimeHuman}</p>
	</div>
</div>

<style>
	div.status {
		margin-top: 32px;
		margin-bottom: 32px;
	}
</style>
