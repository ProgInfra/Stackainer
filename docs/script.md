# Stackainer : Script

![Icon](../icon.png)

## Table Of Contents

- [Stackainer : Script](#stackainer--script)
  - [Table Of Contents](#table-of-contents)
  - [Ideas](#ideas)

## Ideas

- Stackainer Script :
  - Version Support (upgrade possibility with question and task todo) / Use of real version or use Git Commit of file ?
  - Update : Git clone / pull to get update
  - Upgrade : Compare default.env file and new default.env file
  - Init a Stackainer System
  - Start, Stop services
  - Add, Remove services (when add, configure some .env file)
  - List installed and available services
  - Docker in Swarm mode
  - Docker Secrets enable with _SECRET at the end of the .env
- Commands :
  - init : Create a new directory to store stackainer files (git repo clone, created stack, datas)
  - list : List services (by category, installed or available)
  - install : Install new services and prompt question to fill .env file from .env.default file
  - remove : Stop and delete services installed
  - start : Start services (by category, by name, all)
  - stop : Stop services (by category, by name, all)
  - update : Update Stackainer repository
  - upgrade : Compare default.env file and new default.env file to replace older versions installed

db.py
__init__.py
models.py
stackainer.py
stack.py
tes
update.py
utils.py
