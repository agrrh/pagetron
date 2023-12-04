import statistics

from prometheus_api_client import PrometheusConnect
from prometheus_api_client.utils import parse_datetime

from typing import List

from lib.view import ViewPreset, timestamp_to_human_token


class DBInterface(object):
    def __init__(self, addr="http://127.0.0.1:9090/"):
        self.addr = addr
        self.client = PrometheusConnect(
            url=addr,
            disable_ssl=(not addr.startswith("https://")),
        )

    def get_overview(self) -> dict:
        raw_data = self.client.custom_query(
            query="sum by (instance) (pagetron:availability:1m)"
        )

        # [
        #     {
        #         'metric': {'instance': 'https://example.org'},
        #         'value': [1701553944.544, '1']
        #     },
        #     {...}
        # ]

        statuses_list = []
        components_issues_list = []

        timestamp = raw_data[0].get("value", [0, "0.0"])[0]

        for m in raw_data:
            name = m.get("metric", {}).get("instance")
            status = m.get("value", [0, "0"])[1] == "1"

            statuses_list.append(status)
            if not status:
                components_issues_list.append(name)

        return {
            "status": all(statuses_list),
            "components_count": len(statuses_list),
            "issues_count": len(components_issues_list),
            "components_issues": components_issues_list,
            "datetime_human": timestamp_to_human_token(timestamp, "datetime"),
        }

    def list_components(self) -> List[str]:
        raw_data = self.client.custom_query(
            query="group by (instance) (pagetron:availability:1m)"
        )

        # [
        #     {
        #         'metric': {'instance': 'https://example.org'},
        #         'value': [1701553944.544, '1']
        #     },
        #     {...}
        # ]

        result = [m.get("metric", {}).get("instance") for m in raw_data]
        result = [_ for _ in result if _]

        return result

    def get_component(self, name: str, view="quarter") -> dict:
        VIEW_PRESETS = {
            "day": ViewPreset(
                depth=24,
                unit="h",
                step="15m",
                metric="pagetron:availability:1m",
                precision="time",
            ),
            "week": ViewPreset(
                depth=7,
                unit="d",
                step="3h",
                metric="pagetron:availability:1h",
                precision="datetime",
            ),
            "month": ViewPreset(
                depth=30,
                unit="d",
                step="12h",
                metric="pagetron:availability:1d",
                precision="datetime",
            ),
            "quarter": ViewPreset(
                depth=90,
                unit="d",
                step="1d",
                metric="pagetron:availability:1d",
                precision="date",
            ),
            "year": ViewPreset(
                depth=365,
                unit="d",
                step="7d",
                metric="pagetron:availability:1d",
                precision="date",
            ),
        }

        if view not in VIEW_PRESETS:
            raise ValueError

        preset = VIEW_PRESETS.get(view)

        start_time = parse_datetime(f"{preset.depth}{preset.unit}")
        end_time = parse_datetime("now")

        metric_data = self.client.custom_query_range(
            query=f'sum(avg_over_time({preset.metric}{{instance="{name}"}}[{preset.step}]) or on() vector(-1))',
            start_time=start_time,
            end_time=end_time,
            step=preset.step,
        )

        # [
        #     {
        #         'metric': {'__name__': 'pagetron:availability:1h', 'instance': 'https://example.org'},
        #         'values': [
        #             [1701548820.431, '0.4666666666666667'],
        #             [1701552420.431, '1'],
        #             [1701556020.431, '0.9666666666666667'],
        #         ]
        #     }
        # ]

        if not metric_data:
            raise ValueError

        data = [
            (
                timestamp_to_human_token(v[0], preset.precision),
                round(float(v[1]), 5),
            )
            for v in metric_data[0].get("values", [])
        ]

        statistics_values = [v[1] for v in data if v[1] >= 0.0] or [0.0]
        uptime = round(statistics.mean(statistics_values), 5)

        return {
            "name": name,
            "uptime": uptime,
            "observations": data,
        }
