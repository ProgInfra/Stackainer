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

1) TODO Clone the Repository
2) TODO Auto Script with choice ?
3) TODO Choose Type of Stack
4) TODO Delete Services you don't want
5) TODO Configure each services with .env files
6) TODO Use script to launch the stack and stop the stack
7) TODO Verify each services

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
  - [ ] [Traefik Proxy V2](https://traefik.io/traefik/) : Cloud Native Application Proxy.

### Management Stack

- [**Management Stack**](./docs/management.md) :
  - [ ] [Portainer](https://www.portainer.io/) (**Port** : TODO / **Base URL** : TODO) : Container Management.

### Storage Stack

- [**Storage Stack**](./docs/storage.md) :
  - [ ] [Minio](https://min.io/) (**Port** : TODO / **Base URL** : TODO) : Multi-Cloud Object Storage (S3 API Compatible).

### Backup Stack

- [**Backup Stack**](./docs/backup.md) :
  - [ ] [Duplicati](https://www.duplicati.com/) (**Port** : TODO / **Base URL** : TODO) : Global Backup software.
  - [ ] [Docker DB Backup](https://github.com/tiredofit/docker-db-backup) (**Port** : TODO / **Base URL** : TODO) : Auto Backup multiple types of Databases.

### Monitoring Stack

- [**Monitoring Stack**](./docs/monitoring.md) :
  - [ ] [Prometheus](https://prometheus.io/) (**Port** : TODO / **Base URL** : TODO) : Metrics recorder.
  - [ ] [Grafana](https://grafana.com/) (**Port** : TODO / **Base URL** : TODO) : Great Metrics visualizer with Dashboard.
  - [ ] [cAdvisor](https://github.com/google/cadvisor) (**Port** : TODO / **Base URL** : TODO) : Sensor to get metrics from container.
  - [ ] [Node Exporter](https://github.com/prometheus/node_exporter) (**Port** : TODO / **Base URL** : TODO) : Sensor to get metrics from hardware and OS.
  - [ ] [Alert Manager](https://github.com/prometheus/alertmanager) (**Port** : TODO / **Base URL** : TODO) : Handles alerts and send notifications to clients.
  - [ ] [Unsee](https://github.com/cloudflare/unsee) (**Port** : TODO / **Base URL** : TODO) : Alert Dashboard for Alert Manager.
  - [ ] [Uptime Kuma](https://github.com/louislam/uptime-kuma) (**Port** : TODO / **Base URL** : TODO) : Web App to Check Uptime of website or services.
  - [ ] [Watchtower](https://github.com/containrrr/watchtower) (**Port** : TODO / **Base URL** : TODO) : Automating Docker Container Updates.
  - [ ] [Scrutiny](https://github.com/AnalogJ/scrutiny) (**Port** : TODO / **Base URL** : TODO) : SMART Monitoring.

### Access Stack

- [**Access Stack**](./docs/access.md) :
  - [ ] [Heimdall](https://heimdall.site/) (**Port** : TODO / **Base URL** : TODO) : Applications Dashboard.
  - [ ] [Organizr](https://organizr.app/) (**Port** : TODO / **Base URL** : TODO) : Services portal.
  - [ ] [Pi-Hole](https://pi-hole.net/) (**Port** : TODO / **Base URL** : TODO) : Network-wide Ad Blocking.
  - [ ] [WireGuard](https://www.wireguard.com/) (**Port** : TODO / **Base URL** : TODO) : Fast, Modern and Secure VPN Tunnel.
  - [ ] [WG-Manager](https://github.com/perara/wg-manager) (**Port** : TODO / **Base URL** : TODO) : Manage WireGuard with web UI.

### Security Stack

- [**Security Stack**](./docs/security.md) :
  - [ ] [Authentik](https://goauthentik.io/) (**Port** : TODO / **Base URL** : TODO) : Open Source Identity Provider.
  - [ ] [VaultWarden](https://github.com/dani-garcia/vaultwarden) (**Port** : TODO / **Base URL** : TODO) : Alternative of Bitwarden server in Rust compatible with Bitwarden clients.

### Media Stack

- [**Media Stack**](./docs/media.md) :
  - [ ] [Jellyfin](https://jellyfin.org/) (**Port** : TODO / **Base URL** : TODO) : Open Source Media System.
  - [ ] [MiniFlux](https://miniflux.app/) (**Port** : TODO / **Base URL** : TODO) : Minimalist and opinionated feed reader.
  - [ ] [Kavita](https://www.kavitareader.com/) (**Port** : TODO / **Base URL** : TODO) : Digital Ebook Livrary.

### Download Stack

- [**Download Stack**](./docs/download.md) :
  - [ ] [Transmission Control](https://gitlab.com/proginfra/transmission_control) (**Port** : TODO / **Base URL** : TODO) : Transmission with VPN support and an advanced Web GUI.
  - [ ] [Jackett](https://github.com/Jackett/Jackett) (**Port** : TODO / **Base URL** : TODO) : Tracker Site Manager.
  - [ ] [MeTube](https://github.com/alexta69/metube) (**Port** : TODO / **Base URL** : TODO) : Web GUI for youtube-dl (using the yt-dlp fork).
  - [ ] [pyLoad](https://pyload.net/) (**Port** : TODO / **Base URL** : TODO) : Great Download Manager.
  - [ ] HakuNeko Docker : Manga Downloader with Web UI.

### Utility Stack

- [**Utility Stack**](./docs/utility.md) :
  - [ ] [The Lounge](https://thelounge.chat/) (**Port** : TODO / **Base URL** : TODO) : Web IRC Client
  - [ ] [Grocy](https://github.com/grocy/grocy) (**Port** : TODO / **Base URL** : TODO) : Food Management.
  - [ ] [ProjectSend](https://www.projectsend.org/) (**Port** : TODO / **Base URL** : TODO) : Upload and Share Application.

### Development Stack

- [**Development Stack**](./docs/development.md) :
  - [ ] [PostgreSQL](https://www.postgresql.org/) (**Port** : TODO / **Base URL** : TODO) : Advanced SQL Database with PL/SQL (Oracle alternative).
  - [ ] [pgAdmin](https://www.pgadmin.org/) (**Port** : TODO / **Base URL** : TODO) : PostgreSQL Tools.
  - [ ] [MariaDB](https://mariadb.org/) (**Port** : TODO / **Base URL** : TODO) : Open Source SQL Database.
  - [ ] [MySQL](https://www.mysql.com/) (**Port** : TODO / **Base URL** : TODO) : SQL Database.
  - [ ] [Adminer](https://www.adminer.org/) (**Port** : TODO / **Base URL** : TODO) : SQL Database Tools.
  - [ ] [PHPMyAdmin](https://www.phpmyadmin.net/) (**Port** : TODO / **Base URL** : TODO) : SQL Database Tools.
  - [ ] [MongoDB](https://www.mongodb.com/) (**Port** : TODO / **Base URL** : TODO) : NoSQL Database.
  - [ ] [Mongo Express](https://github.com/mongo-express/mongo-express) (**Port** : TODO / **Base URL** : TODO) : NoSQL Database Tools for MongoDB.

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
docker-compose -f docker-compose.dev.yml up

# Production
docker-compose up --build
```

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE) for more information.
