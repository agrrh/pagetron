from pydantic import BaseModel

from datetime import datetime


class ViewPreset(BaseModel):
    depth: int
    unit: str = "m"
    step: str = "1m"
    metric: str = "pagetron:availability:1m"
    precision: str = "time"


def timestamp_to_human_token(ts, precision="datetime"):
    dt = datetime.fromtimestamp(ts)

    dt_fmt = {
        "datetime": "%b %d, %Y at %H:%M",
        "time": "%H:%M",
        "date": "%b %d, %Y",
    }.get(precision)

    return dt.strftime(dt_fmt)
