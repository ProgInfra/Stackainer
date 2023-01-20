class Service:
    '''
    Service model class.
    '''
    name = None
    version = None
    # Type Enum [Port / Traefik]
    type = None
    # Type Enum [docker / swarm]
    engine = None
    variables = []
    secrets = []

    def from_file(filename: str):
        '''
        Parse Service from .env file.
        '''
        pass

    def to_file(filename: str):
        '''
        Save Service to .env file.
        '''
        pass
