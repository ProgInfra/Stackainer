# Import created libraries
from .parameters import DeployType, Categories


class Port:
    '''
    Service Port.
    '''
    name: str
    port: int


class Domain:
    '''
    Service Domain.
    '''
    name: str
    domain: str


class Variable:
    '''
    Service Variable.
    '''
    name: str
    value: str
    tips: list(str)


class Secret:
    '''
    Service Secret.
    '''
    name: str
    value: str
    tips: list(str)


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
    urls: list(Domain) = []
    variables: list(Variable) = []
    secrets: list(Secret) = []
