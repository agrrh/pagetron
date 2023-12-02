<script>
import humanizeDuration from 'humanize-duration'

export let id = "01.01";
export let uptime = 0.0;
export let capacitySeconds = 86400; // Seconds in each day
export let thresholds = [0.990, 0.950]

let tickStateClasses = "";

if (uptime > thresholds[0]) {
	tickStateClasses = "has-background-success";
} else if (uptime > thresholds[1]) {
	tickStateClasses = "has-background-warning";
} else {
	tickStateClasses = "has-background-danger";
}

let downtime = Math.round((1.0 - uptime) * capacitySeconds);
let downtimeHuman = humanizeDuration(downtime, { maxDecimalPoints: 1, units: ["h", "m", "s"] });
</script>

<div
	class="
		tick
		has-tooltip-arrow
		has-tooltip-text-centered
		{tickStateClasses}
	"
	data-tooltip="{id}
down for {downtimeHuman}"
>
</div>

<style>
div.tick {
	display: block;
	margin-right: 1px;
	width: 1.1%;
	height: 24px;
}

div.tick:hover {
	border: 1px solid black;
}
</style>
