# Stackainer

![Icon](./icon.png)

[Stack icons created by Ivan Abirawa - Flaticon](https://www.flaticon.com/free-icons/stack)

## Table Of Contents

- [Stackainer](#stackainer)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Access](#access)
  - [Getting Started](#getting-started)
  - [Type of Stack Available](#type-of-stack-available)
  - [Stack Available](#stack-available)
    - [Depends Stack](#depends-stack)
    - [Management Stack](#management-stack)
    - [Storage Stack](#storage-stack)
    - [Backup Stack](#backup-stack)
    - [Monitoring Stack](#monitoring-stack)
    - [Access Stack](#access-stack)
    - [Security Stack](#security-stack)
    - [Media Stack](#media-stack)
    - [Download Stack](#download-stack)
    - [Utility Stack](#utility-stack)
    - [Development Stack](#development-stack)
  - [Changelog](#changelog)
  - [Documentations](#documentations)
  - [Development](#development)
    - [Requirements](#requirements)
    - [Docsify](#docsify)
  - [Contributing](#contributing)
  - [Licence](#licence)

## Description

**Stack** of **Container** to deploy **services**.

This project **regroup** a **lot of services available** on **Docker** (mainly **web services**), the objective of this project is to propose to you the possibility to **create** your **own stack** with a package of services and a **script** to run this stack.

## Access

- **Development (Local)** :
  - [Stackainer Docs Development](http://localhost:6007)
- **Production (Local)** :
  - [Stackainer Docs Production](http://localhost:6007)
- **Production** :
  - [Stackainer Docs Production](https://proginfra.gitlab.io/stackainer)

## Getting Started

TODO Script Staickainer

## Type of Stack Available

There are several type of stack available with same services but configured differently with some features for each type of stack :

- **Port Type** : **Basic Stack** with just a **port mapping** for each **services** on **Single Docker Machine**.
- **Traefik Type** : **Stack** with **Traefik** as main **Reverse Proxy** to use a **domain name** and **HTTPS** to access each services on **Single Docker Machine**.
- **Swarm Traefik Type** : **Advanced Stack**, same as **Traefik Type** but with **Swarm Orchestrator** to deploy the stack on a **Cluster** of **Docker Machine**.

## Stack Available

Each stack have a lot of **services available** (if **checked**) or in futur (if **unchecked**).

### Depends Stack

**Depends** is an **important Stack** to setup some **services** before all other like **Traefik** which is needed for each services.

- [**Depends Stack**](./docs/depends.md) :
  - [TODO] [Traefik Proxy V2](https://traefik.io/traefik/) : Cloud Native Application Proxy.
    - **Port** : 80 (HTTP) / 443 (HTTPS)
    - **Base URL** : proxy.DOMAIN

### Management Stack

- [**Management Stack**](./docs/management.md) :
  - [TODO] [Portainer](https://www.portainer.io/) : Container Management.
    - **Port** : TODO
    - **Base URL** : TODO

### Storage Stack

- [**Storage Stack**](./docs/storage.md) :
  - [ ] [Minio](https://min.io/) : Multi-Cloud Object Storage (S3 API Compatible).

### Backup Stack

- [**Backup Stack**](./docs/backup.md) :
  - [TODO] [Duplicati](https://www.duplicati.com/) : Global Backup software.

### Monitoring Stack

- [**Monitoring Stack**](./docs/monitoring.md) :
  - [ ] [NetData](https://www.netdata.cloud/) : Automated and easy monitoring everything on server.
  - [TODO] [Prometheus](https://prometheus.io/) : Metrics recorder.
  - [TODO] [Grafana](https://grafana.com/) : Great Metrics visualizer with Dashboard.
  - [TODO] [cAdvisor](https://github.com/google/cadvisor) : Sensor to get metrics from container.
  - [TODO] [Node Exporter](https://github.com/prometheus/node_exporter) : Sensor to get metrics from hardware and OS.
  - [ ] [Alert Manager](https://github.com/prometheus/alertmanager) : Handles alerts and send notifications to clients.
  - [ ] [Unsee](https://github.com/cloudflare/unsee) : Alert Dashboard for Alert Manager.
  - [TODO] [Uptime Kuma](https://github.com/louislam/uptime-kuma) : Web App to Check Uptime of website or services.
  - [TODO] [Watchtower](https://github.com/containrrr/watchtower) : Automating Docker Container Updates.
  - [ ] [Scrutiny](https://github.com/AnalogJ/scrutiny) : SMART Monitoring.

### Access Stack

- [**Access Stack**](./docs/access.md) :
  - [TODO] [Heimdall](https://heimdall.site/) : Applications Dashboard.
  - [ ] [Organizr](https://organizr.app/) : Services portal.
  - [ ] [Dashy](https://dashy.to/) : Ultimate Homepage for Homelab.
  - [ ] [Pi-Hole](https://pi-hole.net/) : Network-wide Ad Blocking.
  - [TODO] [WireGuard](https://www.wireguard.com/) : Fast, Modern and Secure VPN Tunnel.
  - [TODO] [WG-Manager](https://github.com/perara/wg-manager) : Manage WireGuard with web UI.

### Security Stack

- [**Security Stack**](./docs/security.md) :
  - [ ] [Authentik](https://goauthentik.io/) : Open Source Identity Provider.
  - [TODO] [Vaultwarden](https://github.com/dani-garcia/vaultwarden) : Alternative of Bitwarden server in Rust compatible with Bitwarden clients.

### Media Stack

- [**Media Stack**](./docs/media.md) :
  - [ ] [Jellyfin](https://jellyfin.org/) : Open Source Media System.
  - [ ] [Pydio Cells](https://pydio.com/) : Files Cloud.

### Download Stack

- [**Download Stack**](./docs/download.md) :
  - [TODO] [Transmission Control](https://gitlab.com/proginfra/transmission_control) : Transmission with VPN support and an advanced Web GUI.
  - [ ] [DLeaderr](https://gitlab.com/proginfra/dleaderr) : Coordinator to use with Jackett as Torrent Indexer and Transmission as Torrent Downloader.
  - [TODO] [Jackett](https://github.com/Jackett/Jackett) : Tracker Site Manager.
  - [ ] [MeTube](https://github.com/alexta69/metube) : Web GUI for youtube-dl (using the yt-dlp fork).
  - [ ] [pyLoad](https://pyload.net/) : Great Download Manager.
  - [ ] HakuNeko Docker : Manga Downloader with Web UI.

### Utility Stack

- [**Utility Stack**](./docs/utility.md) :
  - [ ] [The Lounge](https://thelounge.chat/) : Web IRC Client
  - [ ] [Grocy](https://github.com/grocy/grocy) : Food Management.
  - [ ] [Monica](https://github.com/monicahq/monica) : Personal Relationship Manager.
  - [TODO] [ProjectSend](https://www.projectsend.org/) : Upload and Share Application.
  - [ ] [Firefly III](https://www.firefly-iii.org/) : Open Source Personal Finance Manager.
  - [ ] [Searx](https://searx.github.io/searx/) : Free Search Engine.
  - [ ] [Wallabag](https://github.com/wallabag/wallabag) : Web Application to save web pages.
  - [TODO] [Planka](https://planka.app/) : Open Source Kanban board.
  - [ ] [Taiga.io](https://github.com/taigaio/) : Kanban Board.
  - [ ] [Wekan](https://github.com/wekan/wekan) : Kanban Board.
  - [ ] [Kanboard](https://github.com/kanboard/kanboard) : Kanban Board.

### Development Stack

- [**Development Stack**](./docs/development.md) :
  - [ ] [PostgreSQL](https://www.postgresql.org/) : Advanced SQL Database with PL/SQL (Oracle alternative).
  - [ ] [pgAdmin](https://www.pgadmin.org/) : PostgreSQL Tools.
  - [ ] [MariaDB](https://mariadb.org/) : Open Source SQL Database.
  - [ ] [MySQL](https://www.mysql.com/) : SQL Database.
  - [ ] [Adminer](https://www.adminer.org/) : SQL Database Tools.
  - [ ] [PHPMyAdmin](https://www.phpmyadmin.net/) : SQL Database Tools.
  - [ ] [MongoDB](https://www.mongodb.com/) : NoSQL Database.
  - [ ] [Mongo Express](https://github.com/mongo-express/mongo-express) : NoSQL Database Tools for MongoDB.

## Changelog

See [CHANGELOG](./CHANGELOG.md) for more information.

## Documentations

- [Ideas](./docs/ideas.md)
- [Resources](./docs/resources.md)

## Development

If you want you can **develop** this repository :

1) You need to install the [Requirements](#requirements)
2) You can develop on [Docsify](#docsify)

### Requirements

We use **Docker** :

- Docker
- Docker Compose

### Docsify

```bash
cd docsify

# Development
docker compose -f docker-compose.dev.yml up

# Production
docker compose up --build
```

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE) for more information.
