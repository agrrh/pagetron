# Pagetron

Free status page generator you always wanted!

## About The Project

Uses well-known technologies

  - Prometheus under the hood
  - Kubernetes-ready

Built with modular architecture in mind

  - Easy to build e.g. your own UI

Free to use and extend

  - Released under [WTFPL](https://ru.wikipedia.org/wiki/WTFPL), one of most permissive licenses

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

Platform

  - [Docker](https://www.docker.com/)
  - [Kubernetes](https://kubernetes.io/)

Frontend


  - [Svelte](https://svelte.dev)

Backend

  - [FastAPI](https://fastapi.tiangolo.com/)

Storage

  - [Prometheus](https://prometheus.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

You must have Kubernetes cluster to be up and running to deploy this application in native way.

You also may run it with Docker and possibly Docker Compose, after translating k8s manifests to docker or docker-compose scenario.

See [./deploy](./deploy) folder.

### Installation

⚠️ Development stage.

At the moment, installation is as simple as:

```
kubectl apply -R -f ./deploy
```

This will create some resources in your cluster:

- Namespace `"pagetron"`
- Configmaps
- Deployments
- PVC with default StorageClass
- Services
- ...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

⚠️ Development stage.

### Setting up monitoring

To monitor your stuff, you must target metrics collector (currently, `blackbox` exporter) to desired resources in `deploy/prometheus/prometheus.configmap.yaml`:

```
- targets:
  - https://example.org
  - https://api.example.org
```

### Backend

First, expose metrics on your local environment:

```
kubectl port-forward -n pagetron svc/prometheus 9090:9090
```

Then run backend API:

```
cd backend

docker build . -t local/pagetron:backend
docker run --rm -ti --network host local/pagetron:backend
```

### Frontend

Just run frontend:

```
npm i
npm run dev
```

Then you may visit UI:

http://localhost:5173/

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] [Prototype Stage](https://github.com/agrrh/pagetron/milestone/1)
- [ ] [Core Features](https://github.com/agrrh/pagetron/milestone/2)
- [ ] [Nice To Have](https://github.com/agrrh/pagetron/milestone/3)

See the [open issues](https://github.com/agrrh/pagetron/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feat/some-useful-stuff`)
3. Commit your Changes (`git commit -m 'Add some useful stuff'`)
4. Push to the Branch (`git push origin feat/some-useful-stuff`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the [WTFPL](https://wikipedia.org/wiki/WTFPL) License. See [LICENSE.md](LICENSE.md) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contacts

Project Link: [https://github.com/agrrh/pagetron](https://github.com/agrrh/pagetron)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

Some inspiration from great services:

- [Better Stack](https://betterstack.com)
- [OneUptime](https://oneuptime.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
