# Import installed libraries
import typer

# Import created librairies
import utils


# Init Typer
app = typer.Typer()


@app.command()
@utils.typer_async
async def update():
    '''
    Update stackainer.
    '''
    pass


@app.command()
@utils.typer_async
async def upgrade():
    '''
    Upgrade services.
    '''
    pass
