#### Fast api example

Configure Venv

`pip install virtualenv`

`python<version> -m venv <virtual-environment-name>`

`source env/bin/activate.fish`

Run fastapi

uvicorn main:app --reload

**Informations about FastAPI**
Fast api uses asgi which handles requests asyncronously

Flask wsgi which handles requests syncronously