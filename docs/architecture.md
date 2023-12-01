# Architecture

```mermaid
graph LR

visitor

subgraph resources
  website[website]
  api[API]
end

subgraph kubernetes
  blackbox[blackbox-exporter]

  prometheus

  prometheus -.-> |checks| blackbox
  blackbox -.->  |probe| website & api

  app -.- |get data| prometheus
end

visitor -.-> app
```
