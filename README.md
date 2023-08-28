# Core

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

### Local Development
1. `cd /project_folder`
2. `cd backend/`
3. `python3 -m venv venv_dev` (create the global formatting venv)
4. remove `.sample` from each services `.envrc.sample` and replace defaults
5. `direnv allow` from backend root dir
6. Install requirements for `venv_dev` (global formatting `venv`)
```
pip install -r requirements-dev.txt
```

Navigate to each service and perform the following:
6. `cd _service/`
7. `python3 -m venv venv`
8. `direnv allow` in each service (if using envrc)
9. install requirements for each `venv`
```
pip install -r requirements.txt
```

9. Use VSCode workspace to open project, then set interpreter path for each workspace venv (unless vscode correctly interprets)


### Docker
1. Start Docker daemon (colima or default docker desktop)
2. Navigate to root `backend/`
3. Start docker process with docker-compose (w/wo `--build`):
```
docker-compose up --build
```

### Useful Docker commands
```
docker exec -it `container_name/id` psql -U ethancavill -d `db_name: auth_db/core_db`
docker exec -it `container_name/id` alembic revision --autogenerate -m "Migration message goes here"
docker exec -it `container_name/id` alembic upgrade head

docker logs -f `container_name/id`
docker volume ls
docker ps
```

`docker exec -it` - exec commands in a running container (it~>interact)

### Dbeaver connection
Host: `0.0.0.0`
Port: `5432`
