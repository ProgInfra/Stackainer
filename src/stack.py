# Import installed libraries
import typer

# Import created librairies
import utils


# Init Typer
app = typer.Typer()


@app.command()
@utils.typer_async
async def install():
    '''
    Install a service.
    '''
    pass


@app.command()
@utils.typer_async
async def remove():
    '''
    Remove a service.
    '''
    pass


@app.command()
@utils.typer_async
async def start():
    '''
    Start some service or stack.
    '''
    pass


@app.command()
@utils.typer_async
async def stop():
    '''
    Stop some service or stack.
    '''
    pass
