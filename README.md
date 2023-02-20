# Stackainer

![Icon](./icon.png)

[Stack icons created by Ivan Abirawa - Flaticon](https://www.flaticon.com/free-icons/stack)

## Table Of Contents

- [Stackainer](#stackainer)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Access](#access)
  - [Getting Started](#getting-started)
  - [Type of Deployment Available](#type-of-deployment-available)
  - [Stack Available](#stack-available)
    - [Management Stack](#management-stack)
    - [Storage Stack](#storage-stack)
    - [Backup Stack](#backup-stack)
    - [Monitoring Stack](#monitoring-stack)
    - [Access Stack](#access-stack)
    - [Security Stack](#security-stack)
    - [Game Stack](#game-stack)
    - [Media Stack](#media-stack)
    - [Download Stack](#download-stack)
    - [Utility Stack](#utility-stack)
    - [Development Stack](#development-stack)
    - [Miscellaneous](#miscellaneous)
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

TODO Documentation Create new stack ./docs/stack.md

## Type of Deployment Available

There are several deployment possible :

- **Docker** : **Basic Docker** deployment with just a **port mapping** for each **services** on a **Single Docker Machine**.
- **Traefik** : **Deployment** with Traefik as main **Reverse Proxy** to use a **domain name** and **HTTPS** to access each services on a **Single Docker Machine**.
- **Swarm** : **Advanced Deployment**, same as **Traefik Deployment** but with **Swarm Orchestrator** to deploy the stack on a **Cluster** of **Docker Machines**.

## Stack Available

Each stack have a lot of **services available** (if **checked**) or in futur (if **unchecked**).

### Management Stack

- [ ] [Portainer](https://www.portainer.io/) : Container Management.
  - **Port** : TODO
  - **Base URL** : TODO

### Storage Stack

- [ ] [Minio](https://min.io/) : Multi-Cloud Object Storage (S3 API Compatible).
- [ ] [RClone](https://rclone.org/) : Cloud Storage Manager.

### Backup Stack

- [ ] [Duplicati](https://www.duplicati.com/) : Global Backup software.

### Monitoring Stack

- [ ] [NetData](https://www.netdata.cloud/) : Automated and easy monitoring everything on server.
- [ ] [Prometheus](https://prometheus.io/) : Metrics recorder.
- [ ] [Grafana](https://grafana.com/) : Great Metrics visualizer with Dashboard.
- [ ] [cAdvisor](https://github.com/google/cadvisor) : Sensor to get metrics from container.
- [ ] [Node Exporter](https://github.com/prometheus/node_exporter) : Sensor to get metrics from hardware and OS.
- [ ] [Alert Manager](https://github.com/prometheus/alertmanager) : Handles alerts and send notifications to clients.
- [ ] [Unsee](https://github.com/cloudflare/unsee) : Alert Dashboard for Alert Manager.
- [ ] [Uptime Kuma](https://github.com/louislam/uptime-kuma) : Web App to Check Uptime of website or services.
- [ ] [Watchtower](https://github.com/containrrr/watchtower) : Automating Docker Container Updates.
- [ ] [Scrutiny](https://github.com/AnalogJ/scrutiny) : SMART Monitoring.

### Access Stack

- [ ] [Traefik Proxy V2](https://traefik.io/traefik/) : Cloud Native Application Proxy.
  - **Port** : 80 (HTTP) / 443 (HTTPS)
  - **Base URL** : proxy.DOMAIN
- [ ] [Heimdall](https://heimdall.site/) : Applications Dashboard.
- [ ] [Organizr](https://organizr.app/) : Services portal.
- [ ] [Dashy](https://dashy.to/) : Ultimate Homepage for Homelab.
- [ ] [Pi-Hole](https://pi-hole.net/) : Network-wide Ad Blocking.
- [ ] [WireGuard](https://www.wireguard.com/) : Fast, Modern and Secure VPN Tunnel.
- [ ] [WG-Manager](https://github.com/perara/wg-manager) : Manage WireGuard with web UI.

### Security Stack

- [ ] [Keycloak](https://www.keycloak.org/) : Open Source Identity and Access Management.
- [ ] [Vaultwarden](https://github.com/dani-garcia/vaultwarden) : Alternative of Bitwarden server in Rust compatible with Bitwarden clients.

### Game Stack

- [ ] [Crafty Controller](https://craftycontrol.com/) : Open Source Minecraft Server Manager.
- [ ] [PufferPanel](https://www.pufferpanel.com/) : Open Source Game Server Management Panel.

### Media Stack

- [ ] [Jellyfin](https://jellyfin.org/) : Open Source Media System.
- [ ] [Pydio Cells](https://pydio.com/) : Files Cloud.

### Download Stack

- [ ] [Transmission Control](https://gitlab.com/proginfra/transmission_control) : Transmission with VPN support and an advanced Web GUI.
- [ ] [DLeaderr](https://gitlab.com/proginfra/dleaderr) : Coordinator to use with Jackett as Torrent Indexer and Transmission as Torrent Downloader.
- [ ] [Jackett](https://github.com/Jackett/Jackett) : Tracker Site Manager.
- [ ] [MeTube](https://github.com/alexta69/metube) : Web GUI for youtube-dl (using the yt-dlp fork).
- [ ] [pyLoad](https://pyload.net/) : Great Download Manager.
- [ ] HakuNeko Docker : Manga Downloader with Web UI.

### Utility Stack

- [ ] [The Lounge](https://thelounge.chat/) : Web IRC Client
- [ ] [Grocy](https://github.com/grocy/grocy) : Food Management.
- [ ] [Monica](https://github.com/monicahq/monica) : Personal Relationship Manager.
- [ ] [ProjectSend](https://www.projectsend.org/) : Upload and Share Application.
- [ ] [Firefly III](https://www.firefly-iii.org/) : Open Source Personal Finance Manager.
- [ ] [Searx](https://searx.github.io/searx/) : Free Search Engine.
- [ ] [Wallabag](https://github.com/wallabag/wallabag) : Web Application to save web pages.
- [ ] [Planka](https://planka.app/) : Open Source Kanban board.
- [ ] [Taiga.io](https://github.com/taigaio/) : Kanban Board.
- [ ] [Wekan](https://github.com/wekan/wekan) : Kanban Board.
- [ ] [Kanboard](https://github.com/kanboard/kanboard) : Kanban Board.

### Development Stack

- [ ] [PostgreSQL](https://www.postgresql.org/) : Advanced SQL Database with PL/SQL (Oracle alternative).
- [ ] [pgAdmin](https://www.pgadmin.org/) : PostgreSQL Tools.
- [ ] [MariaDB](https://mariadb.org/) : Open Source SQL Database.
- [ ] [MySQL](https://www.mysql.com/) : SQL Database.
- [ ] [Adminer](https://www.adminer.org/) : SQL Database Tools.
- [ ] [PHPMyAdmin](https://www.phpmyadmin.net/) : SQL Database Tools.
- [ ] [MongoDB](https://www.mongodb.com/) : NoSQL Database.
- [ ] [Mongo Express](https://github.com/mongo-express/mongo-express) : NoSQL Database Tools for MongoDB.

### Miscellaneous

- Nothing.

## Changelog

See [CHANGELOG](./CHANGELOG.md) for more information.

## Documentations

- [Ideas](./docs/ideas.md)
- [Resources](./docs/resources.md)
- [New Stack](./docs/stack.md)

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
