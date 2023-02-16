class Service:
    '''
    Service model class.
    '''
    name = None
    version = None
    # Type Enum [Port / Traefik]
    type = None
    # Engine Enum [docker / swarm]
    engine = None
    # Category Enum [TODO]
    category = None
    variables = []
    secrets = []

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
