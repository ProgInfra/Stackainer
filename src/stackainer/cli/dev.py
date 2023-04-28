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
    # Read compose file and check if each .env vars are in the compose file
    # Or extract each variable used in compose file and compare it to the list we have of .env file
    pass
