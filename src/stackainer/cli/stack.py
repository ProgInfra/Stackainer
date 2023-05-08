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
    # Stack Repository : Get and Prompt Variable from Assets
    # Stack Service : Add
    pass


@app.command()
@wrapper.typer_async
async def edit():
    '''
    Edit the configuration of a service
    '''
    # Stack Repository : Get and Prompt Variable to Edit from Stack
    # Stack Service : Edit
    pass


@app.command()
@wrapper.typer_async
async def remove():
    '''
    Remove a service
    '''
    # Stack Repository : Get from Stack
    # Stack Service : Remove
    pass


@app.command()
@wrapper.typer_async
async def start():
    '''
    Start some services
    '''
    # Stack Service : Start
    pass


@app.command()
@wrapper.typer_async
async def stop():
    '''
    Stop some services
    '''
    # Stack Service : Stop
    pass
