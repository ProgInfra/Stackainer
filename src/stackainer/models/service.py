# Import created libraries
from .parameters import DeployType, Categories


class BasicVar:
    '''
    Basic Service Variable.
    '''
    name: str
    value: str
    helpers: list(str)


class Service:
    '''
    Service model class.
    '''
    name = None
    deploy: DeployType = DeployType.docker
    category: Categories = Categories.miscellaneous
    instance = None
    version = None
    depends: list(str) = []
    volumes: list(BasicVar) = []
    ports: list(BasicVar) = []
    urls: list(str) = []
    variables: list(BasicVar) = []
