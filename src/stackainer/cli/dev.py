# Import installed libraries
import typer

# Import created libraries
from ..utils import wrapper


# Init Typer
app = typer.Typer()


@app.command()
@wrapper.typer_async
async def check():
    '''
    Verify if a service have the good format and resume it
    '''
    # Parameters : service name / deploy type / category
    # Read .env file and display informations about the service
    pass
