# Import installed libraries
import typer

# Import created libraries
from . import dev
from . import stack
from ..utils import wrapper
from ..services import stack as StackService


# Init Typer
app = typer.Typer()


@app.command()
@wrapper.typer_async
async def init(name: str, domain: str):
    '''
    Init the stackainer workspace.
    '''
    # Assets Service : Get and Update assets
    await StackService.init(name, domain)


@app.command()
@wrapper.typer_async
async def install():
    '''
    Install current stackainer.
    '''
    # Stack Service : Install
    pass


@app.command()
@wrapper.typer_async
async def list():
    '''
    List available or installed services with query (filters and sorts).
    '''
    # Parameters : name search, deploy types, categories, ... => Filters and Sort !
    # Stack Service : List
    # Display information
    pass


@app.command()
@wrapper.typer_async
async def upgrade():
    '''
    Upgrade installed service.
    '''
    # Stack Service : Upgrade
    pass


app.add_typer(dev.app, name="dev")
app.add_typer(stack.app, name="stack")
