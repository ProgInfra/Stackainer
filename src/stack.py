# Import installed libraries
import typer

# Import created librairies
from models import Service
import utils


# Init Typer
app = typer.Typer()


@app.command()
@utils.typer_async
async def install(service: Service):
    '''
    Install a service.
    '''
    # Copy Service files
    # Edit Service files and prompt variables and secrets
    pass


@app.command()
@utils.typer_async
async def remove(service: Service):
    '''
    Remove a service.
    '''
    # Stop Service
    # Delete Service
    # Update Database file
    pass


@app.command()
@utils.typer_async
async def start(services: list(Service)):
    '''
    Start some service or stack.
    '''
    # Start services
    pass


@app.command()
@utils.typer_async
async def stop(services: list(Service)):
    '''
    Stop some service or stack.
    '''
    # Stop services
    pass
