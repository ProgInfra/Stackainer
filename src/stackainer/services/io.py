# Import installed libraries
from os import path, makedirs, listdir


async def isFileExist(pathFileName: str):
    '''
    Check if the file exist
    '''
    return path.isfile(pathFileName)


async def listFolder(basePath: str):
    '''
    List each folder in path.
    '''
    print(f"List folders in path : {basePath}")
    folders = []
    try:
        folders = listdir(basePath)
    except OSError as error:
        print(f"Error when list folders in path : {basePath}")
        raise error
    print("List complete !")
    return folders


async def listFiles(folderPath: str):
    pass


async def createFolder(folderPath: str):
    '''
    Create folder from path.
    '''
    print(f"Create folder : {folderPath}")
    try:
        makedirs(folderPath, exist_ok=True)
    except OSError as error:
        print(f"Error when create folder : {folderPath}")
        raise error
    print("Create complete !")


async def createFolders(basePath: str, folders: dict, subfolder: bool = False) -> int:
    '''
    Create folders from base path and folders tree.
    '''
    print(f"Create folders in base path : {basePath}")
    folderCounter = 0
    if isinstance(folders, dict):
        for folder in folders:
            folderPath: str = path.join(basePath, folder)
            await createFolder(folderPath)
            folderCounter += 1
            if folders[folder] is not None and isinstance(folders[folder], dict):
                folderCounter += await createFolders(folderPath, folders[folder], True)
    else:
        raise Exception("Bad folders tree format !")
    if not subfolder:
        print(f"Create complete ! ({folderCounter} folders created)")
    return folderCounter


async def writeFile(pathFileName: str, data: str):
    '''
    Write file with data provided
    '''
    try:
        with open(pathFileName, "w") as file:
            file.write(data)
    except IOError as error:
        print(f"Error when write file : {pathFileName}")
        raise error


async def readFile(pathFileName: str):
    pass


async def writeJSONFile(pathFileName: str, data):
    pass


async def readJSONFile(pathFileName: str):
    pass
