# Import standard libraries
from enum import Enum


class DeployType(str, Enum):
    '''
    Type of deployment :
    - Docker for Docker with port mapping
    - Traefik for Docker with Traefik as Reverse Proxy
    - Swarm for Docker Swarm with Traefik as Reverse Proxy
    '''
    docker = "docker"
    traefik = "traefik"
    swarm = "swarm"


class Categories(str, Enum):
    '''
    Service Category.
    '''
    management = "management"
    storage = "storage"
    backup = "backup"
    monitoring = "monitoring"
    access = "access"
    security = "security"
    game = "game"
    media = "media"
    download = "download"
    utility = "utility"
    development = "development"
    miscellaneous = "miscellaneous"
