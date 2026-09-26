# GrafanaStack

A local OpenTelemetry playground: collect logs, metrics, and traces with the
OpenTelemetry Collector, store them in Loki, Mimir, and Tempo, and explore them
in Grafana. Includes a Python dice app and observability MCP endpoints.

Read the [project guide](https://rosmicropy.github.io/GrafanaStack/) for setup,
telemetry examples, configuration, and troubleshooting. The site becomes
available after the first successful Pages deployment.

## Quick start

Install Docker Engine or Docker Desktop with Docker Compose v2, then run:

```sh
git clone https://github.com/ROSMicroPy/GrafanaStack.git
cd GrafanaStack
docker network inspect observe >/dev/null 2>&1 || docker network create observe
docker compose up -d --build
docker compose ps
```

Open [Grafana](http://localhost:3000) (`admin` / `admin`). Anonymous users also
have Admin access. This is a development stack; do not expose it to untrusted
networks. Telemetry is not stored in persistent host volumes.

## Documentation and publishing

The website is plain HTML and CSS in [`pages/`](pages/). Preview locally:

```sh
python3 -m http.server 8088 --directory pages
```

Open [the local guide](http://localhost:8088). Edit `pages/index.html` and
`pages/styles.css` directly; no generator or dependency installation is needed.

In the repository's **Settings → Pages → Build and deployment**, select
**GitHub Actions** as the source (requires repository administration access).
The [Pages workflow](.github/workflows/pages.yml) publishes `pages/` on every
push to `main`, or manually through **Actions → Deploy project guide → Run
workflow** on `main`. A local commit must be pushed before GitHub can deploy it.
If the publishing branch changes, update both branch references in the workflow
and the `github-pages` environment's deployment rules.

The workflow republishes the checked-in guide; update the guide alongside
configuration changes. It does not generate prose from source code.

See [GitHub's custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
for repository setup and deployment permissions.
