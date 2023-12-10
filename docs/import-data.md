# Import historical data

The process is kinda simple, but it takes a few steps to achieve.

## Determine starting timestamp

Let'say, we want to import data for last year.

Today's noon timestamp:

```
$ date +%s -d '1 day ago 12:00'
1702112400
```

Remember this value.

## Format your historical data

Let's say, we have list of uptime values for each day in percentage form, e.g.:

```
[
  100.0,
  99.9,
  ...
  100.0,
]
```

These list must be formatted as OpenMetrics:

```
# TYPE pagetron:availability:1d gauge
pagetron:availability:1d{instance="http://example.org"} 1 1702155600
```

:warning: Note that timestamp in seconds, not in milliseconds!

Here's simple Python script to do so:

```python
# historical_data = [100.0, 99.9, ... , 100.0]
historical_data = []

observed_resource = "https://example.org"
starting_timestamp = 1702112400

with open("backfill_data.txt", "w+") as fp:
    timestamp = starting_timestamp
    for measurement in historical_data:
        value = measurement / 100.0

        openmetrics_line = f"pagetron:availability:1d{{instance=\"{observed_resource}\"}} {value} {timestamp}"
        fp.write(openmetrics_line + "\n")

        timestamp -= 3600 * 24

    fp.write("# EOF" + "\n")

print("done")
```

## Generate blocks for prometheus

```
mkdir backfill_data
promtool tsdb create-blocks-from openmetrics ./backfill_data.txt ./backfill_data
```

Then just move these blocks to prometheus data directory:

```
mv ./backfill_data/* /prometheus/data/
```

Compactor process would optimize them on next run.
