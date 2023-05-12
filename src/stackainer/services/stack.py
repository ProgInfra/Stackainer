# Import installed libraries
from typer import get_app_dir
from dotenv import dotenv_values
import pathlib

# Import created libraries
from ..models import parameters
from . import assets as AssertsService


async def init(name: str, domain: str):
    # Init and create the initial stackainer.json
    # Init with Git and add .gitignore
    # Create folders with GitKeep (assets, stacks, data)
    pass


async def check(
    serviceName: str,
    deployType: parameters.DeployType,
    category: parameters.Categories,
    stackainerPath: str = "."
):
    print(f"Check Service {serviceName} from Category {category} and Deploy Type {deployType}")
    await AssertsService.isExist(serviceName, deployType, category, stackainerPath)
    envFileData = dotenv_values(f"{stackainerPath}/assets/{category}/{serviceName}/{deployType}/.env.sample")
    # Parse EnvFileData to Stack Service
    print(envFileData)


# Refresh : Scan assets and stacks folder to recreate the stackainer.json
# Install : Get and Update Assets and Create Folder
# List : Get Assets and Stack
# Upgrade : Get Assets and Stack, Compare and Prompt to update
# Add : Add Service from assets and configure it
# Edit : Edit Service
# Remove : Remove Service from stack
# Start : Start one or many service
# Stop : Stop one or many service
