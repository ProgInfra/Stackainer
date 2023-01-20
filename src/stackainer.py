# Import installed libraries
import typer

# Import created librairies
import utils


# Init Typer
app = typer.Typer()


@app.command()
@utils.typer_async
async def init():
    '''
    Create the stackainer workspace.
    '''
    # Create new folder for stackainer workspace
    # Git clone and clean folder src
    pass


@app.command()
@utils.typer_async
async def list():
    '''
    List services installed or available.
    '''
    # Get filters (category, search, all)
    # Get installed services with version and information
    # Get available services with version and information
    # Display services with informations
    await utils.launch_command("echo 'Testy'")
    pass


if __name__ == "__main__":
    app()
