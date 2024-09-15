<script>
	import humanizeDuration from 'humanize-duration';

	export let id = '01.01';
	export let uptime = -1.0;
	export let capacity = 60;
	export let thresholds = [0.99, 0.95];

	let units = [];

	function getUnits(capacity) {
		let units = [];

		if (capacity <= 60 * 5) {
			units = ['m', 's'];
		} else if (capacity <= 60 * 60 * 24) {
			units = ['d', 'h', 'm'];
		} else if (capacity <= 60 * 60 * 24 * 7) {
			units = ['w', 'd', 'h'];
		} else {
			units = ['w', 'd'];
		}

		return units;
	}

	let tickStateClasses = '';

	let downtime = 0.0;
	let downtimeHumanText = '';

	function getDowntime(uptime) {
		if (uptime == -1.0) {
			downtime = 1.0 * capacity * 1000; // no data
		} else {
			downtime = Math.round((1.0 - uptime) * capacity) * 1000;
		}

		return downtime;
	}

	function getTickStateClass(uptime) {
		let tickStateClasses;

		if (uptime == -1.0) {
			tickStateClasses = 'has-background-grey';
		} else if (uptime > thresholds[0]) {
			tickStateClasses = 'has-background-success';
			if (downtime > 0) {
				tickStateClasses += ' ' + 'has-minor-issue';
			}
		} else if (uptime > thresholds[1]) {
			tickStateClasses = 'has-background-warning';
		} else {
			tickStateClasses = 'has-background-danger';
		}

		return tickStateClasses;
	}

	function getDowntimeText(uptime) {
		let getDowntimeText;

		if (uptime == 1) {
			downtimeHumanText = '';
		} else if (uptime == -1.0) {
			downtimeHumanText = '\n' + 'no data';
		} else if (downtime > 0) {
			let downtimeHuman = humanizeDuration(downtime, { maxDecimalPoints: 0, units: units });
			downtimeHumanText = '\n' + 'down for ' + downtimeHuman;
		}

		return downtimeHumanText;
	}

	$: downtime = getDowntime(uptime);
	$: units = getUnits(capacity);
	$: downtimeHumanText = getDowntimeText(uptime);
	$: tickStateClasses = getTickStateClass(uptime);
</script>

<div
	class="
		tick
		has-tooltip-arrow
		has-tooltip-text-centered
		has-text-centered
		has-text-white
		{tickStateClasses}
	"
	data-tooltip="{id} {downtimeHumanText}"
></div>

<style>
	div.tick {
		display: block;
		margin: 0px 1px;
		padding: 1px;
		width: 100%;
		height: 24px;
	}

	div.tick:hover {
		box-shadow: inset 0 0 24px 24px rgba(255, 255, 255, 0.5);
	}

	div.tick.has-minor-issue {
		border-top: 5px solid #ffe08a;
	}
</style>
