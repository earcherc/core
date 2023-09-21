# Core
*No longer supported, several mistakes were made :)*

This template provides a foundation for building Python microservices and Next.js 13 web applications, all within a Dockerized environment.


## Planning Doc
- [Google Docs](https://docs.google.com/document/d/1nWxq26N9xc58UbZNNJ4-m58uU7EoFh0y7El0LYVcf4U/edit?usp=sharing)
- [Notion](https://www.notion.so/Main-Microservice-Project-fb97d85962ef45c2bce9fa9714499ec2?pvs=4)

## Backend 
### Deps
- homebrew/nix (package manager)
- direnv
- docker
- docker-compose
- colima/docker desktop (default)
    - colima ipv6 issue https://github.com/abiosoft/colima/issues/583

### Local Development
1. `cd <root_project_folder>/`
2. `cd backend/`
3. `python3 -m venv venv_dev` (create the global formatting venv)
4. remove `.sample` from each services `.envrc.sample` and replace defaults
5. `direnv allow` from backend root dir
6. Install requirements for `venv_dev` (global formatting `venv`)
```
pip install -r requirements-dev.txt
```

Navigate to each service and perform the following:

6. `cd <service>/`
7. `python3 -m venv venv`
8. `direnv allow` in each service (if using envrc)
9. install requirements for each `venv`
```
pip install -r requirements.txt
```
10. install the shared_schemas package in each venv manually
```
pip install ../shared_schemas
```

11.  Use VSCode workspace to open project, then set interpreter path for each workspace venv (unless vscode correctly interprets)


### Docker
1. Start Docker daemon (colima or default docker desktop)
2. Navigate to root `backend/`
3. Start docker process with docker-compose (w/wo `--build`):
```
docker-compose up --build
```

### Useful Docker commands
```
docker exec -it <postgres_db_container_id> psql -U <username> -d <db_name: auth_db/core_db>
docker exec -it <container_id> alembic revision --autogenerate -m "Migration message goes here"
docker exec -it <container_id> alembic upgrade head
docker exec -it <container_id> alembic downgrade -1
docker exec -it <container_id> env
docker exec -it <container_id> /bin/bash

docker-compose restart <service_name>
docker-compose build <service_name>
docker-compose up -d --no-deps --force-recreate <service_name>
docker-compose down
docker logs -f <container_id>
docker-compose logs <service_name: db>
docker volume rm <volume_name>
docker volume ls
docker image ls
docker image prune
docker image prune -a
docker ps
apt-get update && apt-get install curl (install curl in container)
```

`docker exec -it` - exec commands in a running container (it~>interact)

### DBeaver Connection

If you encounter issues while reconnecting to the Dockerized PostgreSQL database, you may need to clear the DBeaver cache. Perform the following:

- Right-click on the connection
- Choose 'Invalidate/Reconnect'

#### Connection Settings

To configure your PostgreSQL database connection in DBeaver, use the following settings:

- **Database**: PostgreSQL
- **Show All Databases**: Check this option

##### Connection Parameters:

| Parameter  | Value            | Description                 |
|------------|------------------|-----------------------------|
| Host       | `0.0.0.0`        | Host address                |
| Port       | `5432`           | Port number                 |
| Database   | `EMPTY`          | Leave this field empty      |
| Username   | `<POSTGRES_USER>`| Replace with actual username|
| Password   | `<POSTGRES_PASSWORD>`| Replace with actual password|
