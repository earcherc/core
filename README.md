# Core

## Planning Doc
- [Google Docs](https://docs.google.com/document/d/1nWxq26N9xc58UbZNNJ4-m58uU7EoFh0y7El0LYVcf4U/edit?usp=sharing)
- [Notion](https://www.notion.so/Main-Microservice-Project-fb97d85962ef45c2bce9fa9714499ec2?pvs=4)

## Backend 
### Deps
- direnv
- docker
- docker-compose

### Local Development
1. cd backend/
2. `python3 -m venv venv_dev`
3. remove `.sample` from all `.envrc.sample`
4. `direnv allow` from root backend dir
5. Install requirements for `venv_dev` (global formatting `venv`)
```
pip install -r requirements-dev.txt
```

Navigate to each service and perform the following:

6. cd `_service`/
7. `python3 -m venv venv`
8. `direnv allow` in each service (if using envrc)
9. install requirements for each `venv`
```
pip install -r requirements.txt
```

9. Use VSCode workspace to open project, then set interpreter path for each workspace venv (unless vscode correctly interprets)


### Docker
1. Start Docker daemon (colima or default)
2. Navigate to `backend/`
3. Run Docker Compose with build:
```
docker-compose up --build
```

### Useful Docker commands
```
docker exec -it backend-auth-1 alembic revision --autogenerate -m "Initial migration"
docker exec -it e5ea076b018d psql -U ethancavill -d auth_db
docker volume ls
docker exec -it backend-auth-1 alembic upgrade head
```

### Dbeaver connection
Host: `0.0.0.0`
Port: `5432`
