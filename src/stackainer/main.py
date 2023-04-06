# Import installed libraries
import typer

# Import created libraries
from .commands import dev
from .commands import stack
from .utils import wrapper


# Init Typer
app = typer.Typer()


@app.command()
@wrapper.typer_async
async def init():
    '''
    Init the stackainer workspace.
    '''
    # Create new folder for stackainer workspace (stacks, data)
    # Git clone and get just src/stacks into assets/*
    # Create stackainer.json
    pass


@app.command()
@wrapper.typer_async
async def install():
    '''
    Update assets and Update stackainer database.
    '''
    # Git clone and get just src/stacks into assets/*
    # Update stackainer.json
    pass


@app.command()
@wrapper.typer_async
async def list():
    '''
    List available or installed services with query (filters).
    '''
    # Read stackainer.json
    # Display information with query
    pass


@app.command()
@wrapper.typer_async
async def upgrade():
    '''
    Upgrade installed service.
    '''
    # Read stackainer.json
    # Compare available services with version to installed services
    # Prompt for upgrade and display changes
    # Update stackainer.json
    pass


app.add_typer(dev.app, name="dev")
app.add_typer(stack.app, name="stack")


if __name__ == "__main__":
    app()
