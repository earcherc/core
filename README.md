# Core

## Planning Doc
- [Google Docs](https://docs.google.com/document/d/1nWxq26N9xc58UbZNNJ4-m58uU7EoFh0y7El0LYVcf4U/edit?usp=sharing)
- [Notion](https://www.notion.so/Main-Microservice-Project-fb97d85962ef45c2bce9fa9714499ec2?pvs=4)

### Local Development

1. Activate venv/allow direnv
2. Install requirements for `venv_dev` (global formatting `venv`) and service `venv`'s
```
pip install -r requirements-dev.txt
pip install -r requirements.txt
```
4. Use VSCode workspace to open project, then set interpreter path for each workspace folder


### Docker
1. Start Docker daemon
2. Navigate to `backend/`
3. Run Docker Compose with build:
```
docker compose up --build
```
