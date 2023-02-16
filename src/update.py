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
    # Delete current src folder of Stackainer
    # Git clone of Stackainer
    # Reload Database
    # Save Database
    pass


@app.command()
@utils.typer_async
async def upgrade():
    '''
    Upgrade services.
    '''
    # Compare Current Service with Newer Service
    # Install it
    pass
