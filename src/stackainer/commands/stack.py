# Import installed libraries
import typer

# Import created libraries
from ..utils import wrapper


# Init Typer
app = typer.Typer()


@app.command()
@wrapper.typer_async
async def add():
    '''
    Add a service and configure it
    '''
    # Read package.json
    # Copy files in assets and read .env file
    # Prompt to configure the service
    pass


@app.command()
@wrapper.typer_async
async def edit():
    '''
    Edit the configuration of a service
    '''
    # Read package.json
    # Read .env file installed
    # Prompt to reconfigure the service
    pass


@app.command()
@wrapper.typer_async
async def remove():
    '''
    Remove a service
    '''
    # Read package.json
    # Stop the service
    # Update package.json
    pass


@app.command()
@wrapper.typer_async
async def start():
    '''
    Start some services
    '''
    # Read package.json
    # Start one or multiple service by query
    pass


@app.command()
@wrapper.typer_async
async def stop():
    '''
    Stop some services
    '''
    # Read package.json
    # Stop one or multiple service by query
    pass
