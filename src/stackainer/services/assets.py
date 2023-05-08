# Import created libraries
from ..models import parameters
from . import io as IOService


async def isExist(
    serviceName: str,
    deployType: parameters.DeployType,
    category: parameters.Categories,
    stackainerPath: str = "."
):
    '''
    Check if the asset exist.
    '''
    envFile = await IOService.isFileExist(f"{stackainerPath}/assets/{category}/{serviceName}/{deployType}/.env.sample")
    if (not envFile):
        raise Exception(
            f"Environment file not found at : {stackainerPath}/assets/{category}/{serviceName}/{deployType}/.env.sample")

    composeFile = await IOService.isFileExist(f"{stackainerPath}/assets/{category}/{serviceName}/{deployType}/compose.yml")
    if (not composeFile):
        raise Exception(
            f"Compose file not found at : {stackainerPath}/assets/{category}/{serviceName}/{deployType}/compose.yml")


async def get(
    serviceName: str,
    deployType: parameters.DeployType,
    category: parameters.Categories,
    forceUpdate: bool = False
):
    # Get Asset and return it with Asset Repository
    if forceUpdate:
        await update()
    pass


async def update():
    # Try to update with Git
    pass
