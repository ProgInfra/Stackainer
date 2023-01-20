# Import standard libraries
from functools import wraps

# Import installed libraries
import asyncio


def typer_async(f):
    '''
    Async Await Wrapper.
    '''
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapper


async def run_command(command: str):
    '''
    Run Command.
    '''
    print(f"Run command : {command}")
    process = await asyncio.create_subprocess_shell(command)
    return process


async def clone_repo():
    '''
    Clone Git Repository.
    '''
    pass


async def create_path(pathToCreate: str):
    '''
    Create path with folders.
    '''
    pass
