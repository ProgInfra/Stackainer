# Stackainer : Stack

![Icon](../icon.png)

## Table Of Contents

- [Stackainer : Stack](#stackainer--stack)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Principe of Stack, Service and Instance](#principe-of-stack-service-and-instance)
  - [ID of a service and instance](#id-of-a-service-and-instance)
  - [Type of Deployment](#type-of-deployment)
  - [Categories](#categories)
  - [Files organisations](#files-organisations)
  - [Environment File](#environment-file)

## Description

When you deploy some **Docker services**, you can use **Docker Compose** files with **.env** files.

## Principe of Stack, Service and Instance

Stackainer use **3** main principe :

- **Stack** : Pack of services sorted by categories.
- **Service** : Docker compose file with pack of container and default configuration.
- **Instance** : Copy of a service with new name and applied custom configuration.

**Example** :

- **Management** is a **stack** which contains **management services**
- **Portainer** is a **service** in **Management Stack**
- **Portainer** (development) is an instance of the **Portainer** service with applied **custom** configuration)

With the instance principe, we can had multiple same services but for different use, for example :

- **Portainer** (development) is an instance of the **Portainer** service with applied **custom** configuration for development use
- **Portainer** (home) is an instance of the **Portainer** service with applied **custom** configuration for home use
- **Portainer** (local) is an instance of the **Portainer** service with applied **custom** configuration for local use
- **Jellyfin** (music) is an instance of the **Jellyfin** service with applied **custom** configuration for music
- **Jellyfin** (video) is an instance of the **Jellyfin** service with applied **custom** configuration for video

## ID of a service and instance

Each service are unique with **three key** :

- **Name** : portainer
- **Deployment Type** : docker
- **Category** : management
- **Full Name (DEPLOY-CATEGORY-NAME)** : docker-management-portainer

Each instance of a service are unique with **four key** :

- **Name** : portainer
- **Deployment Type** : docker
- **Category** : management
- **Stackainer Name** : home
- **Instance Number** : 0001
- **Full Name with Project Name (DEPLOY-CATEGORY-NAME-STACKAINER-INSTANCE)** : docker-management-portainer-home-0001

## Type of Deployment

When we use Stackainer to deploy some stack and service on a machine, we want to customize the deployment we use, to do this we have type of deployment :

- **Docker** : Classic way with just port mapping to access to our service deployed.
- **Traefik** : Reverse Proxy way with the possibility to use a domain name to get access to our service deployed and securly with HTTPS.
- **Swarm** : Same as Traefik but in Swarm mode, with this we can use Stackainer on a Cluster with scalability.

## Categories

There are some **categories** as **stack** name to **sort** services :

- **Management** : Service to manage something.
- **Storage** : Service to manage many storage system.
- **Backup** : Service to manage backup for data and database.
- **Monitoring** : Service to monitor your system or other.
- **Access** : Service to manage access of many type like VPN or just portal of link.
- **Security** : Service to manage security with user management or blocker.
- **Game** : Service to manage game servers or manager of game servers.
- **Media** : Service to manage media and streaming system.
- **Download** : Service to manage downloader or site backup.
- **Utility** : Service for utility purpose.
- **Development** : Service to help in development.
- **Miscellaneous** : Other services.

## Files organisations

- **assets** : Folder to store the downloaded stacks from the Git repository
  - **.gitkeep** : File to keep this folder in Git
  - **STACK_CATEGORY** :
    - **SERVICE** :
      - **DEPLOY_TYPE** :
        - .env.sample
        - compose.yml
- **stacks** : Folder to store installed stacks with configuration
  - **.gitkeep** : File to keep this folder in Git but without environment file in
  - **STACK_CATEGORY** :
    - **SERVICE** :
      - **DEPLOY_TYPE** :
        - **INSTANCE_NAME** :
          - .env
          - compose.yml
- **data** : Folder to store installed stacks datas
  - **.gitkeep** : File to keep this folder in Git but without data in
  - **STACK_CATEGORY** :
    - **SERVICE** :
      - **DEPOY_TYPE** :
        - **INSTANCE_NAME** :
          - **DOCKER_VOLUME_NAME** : Folder with data of docker volume
- **.gitignore** : File to ignore some files to backup this configuration into a Git repository
- **stackainer.json** : Stackainer instance database

## Environment File

End of variable used (to defined specific variable) :

- **Stackainer specific variables** :
  - **\*_PROJECT_NAME** : Stackainer Project Name (ex: home)
  - **\*_SERVICE_NAME** : Service Name (ex: portainer)
  - **\*_DEPLOY_TYPE** : Deployment Type (ex: docker)
    - **docker** : Docker with port mapping
    - **traefik** : Docker with Traefik as Reverse Proxy
    - **swarm** : Docker Swarm with Traefik as Reverse Proxy
  - **\*_CATEGORY** : Category Used (ex: management)
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
  - **\*_INSTANCE** : Number of of this instance (ex: 0001)
  - **\*_VERSION** : Version of the service config in stackainer (ex: 1.0.0)
  - **\*_DEPEND** : Dependencies services (ex: traefik,grafana,prometheus)
- **Docker specific variables** :
  - **\*_IMG** : Service image name
  - **\*_IMG_TAG** : Service image version
  - **\*_VOLUME\_\*** : Service volumes (ex: VOLUME_CONFIG=./data/config and VOLUME_DATA=./data/db)
  - **\*_PORT\_\*** : Service ports (ex: PORT_DEFAULT=80 for HTTP and PORT_SECURE=443 for HTTPS)
  - **\*_URL\_\*** : Service url (ex: URL_DEFAULT=portainer.DOMAIN)
  - **\*_HELPERS** : Service variables tips if you need some command to generate a UUID for example.
  - **\*** : All other variables will be prompted with a default value as main choice.
