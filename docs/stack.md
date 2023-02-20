# Stackainer : Stack

![Icon](../icon.png)

## Table Of Contents

- [Stackainer : Stack](#stackainer--stack)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Environment File](#environment-file)
  - [Writing new Service](#writing-new-service)

## Description

When you deploy some **Docker services**, you can use **Docker Compose** files with **.env** files and **Docker secret** (only with **Swarm** !).

## Environment File

End of variable used (to defined specific variable) :

- **\*_NAME** : Name of the service (ex: portainer)
- **\*_VERSION** : Version of the service (ex: 1.0.0)
- **\*_DEPLOY** : Type of Deployment :
  - **docker** : Docker with port mapping
  - **traefik** : Docker with Traefik as Reverse Proxy
  - **swarm** : Docker Swarm with Traefik as Reverse Proxy
- **\*_CATEGORY** : Category of the service :
  - **management**
  - **storage**
  - **backup**
  - **monitoring**
  - **access**
  - **security**
  - **game**
  - **media**
  - **download**
  - **utility**
  - **development**
  - **miscellaneous**
- **\*_DEPENDS** : List of dependencies stack (ex: traefik,grafana,prometheus)
- **\*_PORT** : Service ports (ex: 80 for HTTP and 443 for HTTPS)
- **\*_URL** : Service url (ex: portainer)
- **\*_SECRET** : Service secrets, you will have to prompt these when you install the service.
- **\*_SECRET_TIPS** : Service secrets tips if you need some command to generate a password for example.
- **\*** : All other variables will be prompted with a default value as main choice.
- **\*_TIPS** : Service variables tips if you need some command to generate a UUID for example.

## Writing new Service

1) Defined your **service**, you need to create your service folder like this : **stack/STACK_CATEGORY/SERVICE_NAME/DEPLOY_TYPE** (ex: stack/management/portainer/docker)
2) Create the **.env.default** file : stack/management/portainer/docker/**.env.default** :

```bash
# TODO
```

3) Create the **docker-compose.yml** file : stack/management/portainer/docker/**docker-compose.yml** :

```bash
---
# TODO
```
