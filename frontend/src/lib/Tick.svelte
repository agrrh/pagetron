<script>
import humanizeDuration from 'humanize-duration'

export let id = "01.01";
export let uptime = 0.0;
export let capacity = 60;
export let thresholds = [0.990, 0.950]

let tickStateClasses = "";

if (uptime > thresholds[0]) {
	tickStateClasses = "has-background-success";
} else if (uptime > thresholds[1]) {
	tickStateClasses = "has-background-warning";
} else {
	tickStateClasses = "has-background-danger";
}

let downtime = Math.round((1.0 - uptime) * capacity) * 1000;
console.log(downtime);
let downtimeHuman = humanizeDuration(downtime, { maxDecimalPoints: 1, units: ["h", "m"] });
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
	margin: 0px 1px;
	padding: 1px;
	width: 5%;
	height: 24px;
}

div.tick:hover {
  box-shadow: inset 0 0 24px 24px rgba(255, 255, 255, 0.5);
}
</style>
