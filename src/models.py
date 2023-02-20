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


class Port:
    '''
    Service Port.
    '''
    def __init__(self, name: str, port: int) -> None:
        self.name: str = name
        self.port: int = port


class Url:
    '''
    Service URL.
    '''
    def __init__(self, name: str, url: str) -> None:
        self.name: str = name
        self.url: str = url


class Variable:
    '''
    Service Variable.
    '''
    def __init__(self, name: str, value: str, tips: list(str)) -> None:
        self.name: str = name
        self.value: str = value
        self.tips: list(str) = tips


class Secret:
    '''
    Service Secret.
    '''
    def __init__(self, name: str, value: str, tips: list(str)) -> None:
        self.name: str = name
        self.value: str = value
        self.tips: list(str) = tips


class Service:
    '''
    Service model class.
    '''
    name = None
    version = None
    deploy: DeployType = DeployType.docker
    category: Categories = Categories.miscellaneous
    dependencies: list(str) = []
    ports: list(Port) = []
    urls: list(Url) = []
    variables: list(Variable) = []
    secrets: list(Secret) = []

    async def from_file(filename: str):
        '''
        Parse Service from .env file.
        '''
        # Parse .env file
        # Load Service
        pass

    async def to_file(filename: str):
        '''
        Save Service to .env file.
        '''
        # Save to .env file
        pass
