# Stackainer : Database

![Icon](../icon.png)

## Table Of Contents

- [Stackainer : Database](#stackainer--database)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [JSON Database](#json-database)
  - [SQL Database](#sql-database)

## Description

Each instance of stackainer use a **database** :

- As file in **JSON** format stored in **stackainer.json**.
- As SQL Engine with **SQLite** (for file) or **PostgreSQL**.

This database contains the **definition** of each **stacks** you use and setup with some information about each **instances** of Stackainer services.

If you want to **share** your stack, you can just share the file **stackainer.json** (for JSON database use) or your **stackainer.db** (for SQLite database use) or your **PostgreSQL Database Dump**, so **anyone** can recreate the same stack as your but with it's own **data** and **configuration**.

## JSON Database

**JSON Database Structure** :

- **Name** : Name of your **stackainer instance**
- **Version** : Current version of **Stackainer** used
- **Domain** : Domain used for the whole project (only with Traefik)
- **Stacks** : List of stacks with there services sorted by deploy type with all informations extracted from assets folder.
- **Instances** : List of Services **Instances** with all **informations** about it (Object Instance)

Here is an example of a **stackainer.json** file :

```json
{
    "name": "home",
    "version": "1.0.0",
    "domain": "domain.net",
    "stacks": {
        "management": {
            "docker": [
                {
                    "name": "portainer",
                    "category": "management",
                    "deploy-type": "docker",
                    "ports": [{ "default": 9000, "helpers": [] }],
                    "url": [{ "default": "portainer", "helpers": [] }],
                    "variables": [{ "img-tag": "latest", "helpers": [] }]
                }
            ],
            "traefik": [],
            "swarm": []
        }
    },
    "instances": [
        {
            "name": "portainer-home-001",
            "service": "portainer",
            "category": "management",
            "deploy-type": "docker",
            "ports": [{ "default": 9000, "helpers": [] }],
            "url": [{ "default": "portainer", "helpers": [] }],
            "variables": [{ "img-tag": "latest", "helpers": [] }]
        }
    ]
}
```

## SQL Database

TODO SQLite and PostgreSQL
