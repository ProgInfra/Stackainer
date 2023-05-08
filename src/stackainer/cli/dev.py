# Import installed libraries
import typer

# Import created libraries
from ..utils import wrapper
from ..models import parameters
from ..services import stack as StackService


# Init Typer
app = typer.Typer()


@app.command()
@wrapper.typer_async
async def check(
    service_name: str,
    deploy_type: parameters.DeployType = typer.Option("docker", "-d", "--deploy-type"),
    category: parameters.Categories = typer.Option("miscellaneous", "-c", "--category"),
    stackainerPath: str = typer.Option(".", "-s", "--stackainer-path")
):
    '''
    Verify if a service have the good format and resume it
    '''
    await StackService.check(service_name, deploy_type, category, stackainerPath)
