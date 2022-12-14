# Stackainer : Ideas

![Icon](../icon.png)

## Table Of Contents

- [Stackainer : Ideas](#stackainer--ideas)
  - [Table Of Contents](#table-of-contents)
  - [Ideas](#ideas)
  - [Stack Ideas](#stack-ideas)
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

## Ideas

- Script to perform action on each services (each files / docker compose files) : Start and Stop
- Traefik :
  - Mix of File for Middleware and Label for services
  - File for non Docker services
  - Docs for DNS Challenge (Cloudflare)
  - Docs for HTTP Challenge
  - Register in DNS : Use IP of Traefik Server in DNS
- Automatic Script : Ansible / Bash / Typer
- Be Careful to permission

## Stack Ideas

### Management Stack

- [ ] [Yacht](https://github.com/SelfhostedPro/Yacht) : Container Management (better for Template use).
- [ ] [SWIRL](https://github.com/cuigh/swirl) : Container Management (better for Swarm).
- [ ] [Healthchecks](https://healthchecks.io/) : Service for monitoring cron jobs.
- [ ] [Polemarch](https://polemarch.org/) : Service for infrastructure orchestration based on ansible.
- [ ] [Ansible Semaphore](https://ansible-semaphore.com/) : Modern UI for Ansible.
- [ ] [Swarmpit](https://swarmpit.io/) : Container Management (better for Swarm).

### Storage Stack

- [ ] [Portus](https://github.com/SUSE/Portus) : Docker Image Repository Web UI with Authorization system.
- [ ] [Docker Registry](https://docs.docker.com/registry/) : Docker Image Repository.
- [ ] [Docker Registry UI](https://github.com/Joxit/docker-registry-ui) : Docker Image Repository Web UI.

### Backup Stack

- [ ] [Rclone](https://rclone.org/gui/) : Manage file and Cloud storage.
- [ ] [Syncthing](https://syncthing.net/) : Cloud Sync Management.
- [ ] [Docker DB Backup](https://github.com/tiredofit/docker-db-backup) : Auto Backup multiple types of Databases.

### Monitoring Stack

- [ ] [Docker Swarm Visualizer](https://github.com/dockersamples/docker-swarm-visualizer) : Swarm Visualizer.

### Access Stack

- [ ] [Homer](https://github.com/bastienwirtz/homer) : Simple static Homepage
- [ ] [RustDesk](https://rustdesk.com/server/) : Open source virtual / remote desktop.
- [ ] [WG UI](https://github.com/EmbarkStudios/wg-ui) : Basic WireGuard web UI.
- [ ] [WireGuard-UI](https://github.com/ngoduykhanh/wireguard-ui) : WireGuard web UI.
- [ ] [Mistborn](https://gitlab.com/cyber5k/mistborn) : WireGuard and Firewall Management.
- [ ] [Pi-Hole](https://pi-hole.net/) : Network-wide Ad Blocking.

### Security Stack

- [ ] [Keycloak](https://www.keycloak.org/) : Open Source Identity and Access Management.
- [ ] [Authelia](https://www.authelia.com/) : Open Source Authentication and Authorization server and portal.
- [ ] LDAP Server ?

### Media Stack

- [ ] [Plex](https://www.plex.tv/) : Media System.
- [ ] [Mango](https://github.com/getmango/Mango) : Manga server and reader.
- [ ] [Komga](https://komga.org/) : Free and open source comics/mangas media server.
- [ ] [Ubooquity](https://vaemendis.net/ubooquity/) : Comics and Ebooks library.
- [ ] [Calibre Web](https://github.com/janeczku/calibre-web) : Calibre for Ebook but web.
- [ ] [Booksonic Air](http://booksonic.org/) : Audiobooks Media.
- [ ] [Airsonic Advanced](https://github.com/airsonic-advanced/airsonic-advanced) : Music media server.
- [ ] [mStream](https://mstream.io/) : Music media server.
- [ ] [Chevereto](https://github.com/rodber/chevereto-free) : Image Media.
- [ ] [Lychee](https://lycheeorg.github.io/) : Image Media.
- [ ] [Piwigo](http://piwigo.org/) : Image Media.
- [ ] [Nextcloud](https://nextcloud.com/) : Files Cloud.
- [ ] [Owncloud](https://owncloud.com/) : Files Cloud.
- [ ] [Kavita](https://www.kavitareader.com/) : Digital Ebook Livrary.
- [ ] [MiniFlux](https://miniflux.app/) : Minimalist and opinionated feed reader.

### Download Stack

- [ ] [Lidarr](https://github.com/lidarr/lidarr) : Music Auto Downloader.
- [ ] [Headphones](https://github.com/rembo10/headphones) : Music Auto Downloader.
- [ ] [Mylar](https://github.com/mylar3/mylar3) : Comic Book Auto Downloader.
- [ ] [Podgrab](https://github.com/akhilrex/podgrab) : Podcast Auto Downloader.
- [ ] [Youtube-DL Material](https://github.com/Tzahi12345/YoutubeDL-Material) : Youtube and other Video website web Downloader.
- [ ] [AllTube Download](https://github.com/Rudloff/alltube) : HTML GUI for youtube-dl.
- [ ] [Medusa](https://pymedusa.com/) : Automatic Video Library Manager for TV Shows.
- [ ] [DuckieTV](https://github.com/SchizoDuckie/DuckieTV) : Series Planning Management.
- [ ] [SiCKRAGE](https://www.sickrage.ca/) : Automatic Video Library Manager for TV Shows.
- [ ] [Nefarious](https://github.com/lardbit/nefarious) : Movies and Series Auto Downloader.
- [ ] [Radarr](https://github.com/Radarr/Radarr) : Fork of Sonarr but for Movies Auto Downloader.
- [ ] [Sonarr](https://github.com/Sonarr/Sonarr) : Series Auto Downloader.
- [ ] [Bazarr](https://www.bazarr.media/) : Companion to Sonarr and Radarr to download Subtitles.
- [ ] [Focalboard](https://www.focalboard.com/) : Project and Task management.
- [ ] HakuNeko Docker : Manga Downloader with Web UI.

### Utility Stack

- [ ] [Home Assistant](https://www.home-assistant.io/) : Open Source Home Automation.
- [ ] [Jeedom](https://www.jeedom.com/fr/) : Open Source Home Automation.
- [ ] [MotionEye](https://github.com/motioneye-project/motioneye/tree/master) : Basic CCTV Solution.
- [ ] [Shinobi](https://shinobi.video/) : The Open Source CCTV Solution.
- [ ] [Wallabag](https://wallabag.org/en) : Web app to save web pages for later.
- [ ] [Webtop](https://docs.linuxserver.io/images/docker-webtop) : Full desktop environments in container.
- [ ] [Briefkasten](https://github.com/ndom91/briefkasten) : Bookmarking Application.
- [ ] [LinkWarden](https://github.com/Daniel31x13/link-warden) : Bookmark and Archive Management.
- [ ] [Pinry](https://docs.getpinry.com/) : Tiling Image Board.
- [ ] [Shiori](https://github.com/go-shiori/shiori) : Bookmarks manager.
- [ ] [Drawio](https://github.com/jgraph/drawio) : Web app to create diagram.
- [ ] [Freshrss](https://freshrss.org/) : RSS Feeds Management.
- [ ] [HedgeDoc](https://hedgedoc.org/) : Markdown Management.
- [ ] [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) : Archive Paper Document.
- [ ] [The Lounge](https://thelounge.chat/) : Web IRC Client

### Development Stack

- [ ] [Theia](https://github.com/eclipse-theia/theia) : VS Code like on web browser.
- [ ] [Eclipse Che](https://github.com/eclipse/che/) : Workspace server and cloud IDE.
- [ ] [GitLab](https://about.gitlab.com/) : DevOps Platform with Git.
- [ ] [GitLab CI Runner](https://docs.gitlab.com/runner/) : CI Runner for GitLab.
- [ ] [OAX](https://github.com/darosh/oax) : OpenAPI Specification Explorer.
- [ ] [Hasura](https://hasura.io/) : Instant GraphQL on all your data.
- [ ] [Open Source JFrog Artifactory](https://jfrog.com/community/open-source/) : Universal Artifact Repository.
- [ ] [Ghost](https://ghost.org/) : Blogging platform.
- [ ] [Drone](https://www.drone.io/) : CI / CD Self Hosted.
- [ ] [Gitea](https://gitea.io/en-us/) : A painless self-hosted Git service.
- [ ] [OpenVSCode Server](https://github.com/gitpod-io/openvscode-server) : VS Code on web browser (used by GitHub).
- [ ] [Code Server](https://github.com/coder/code-server) : VS Code on web browser.
- [ ] [Cloud9](https://github.com/c9/core) : Web IDE.
- [ ] [NetBox](https://github.com/netbox-community/netbox) : Network Infrastructure Modeling.
