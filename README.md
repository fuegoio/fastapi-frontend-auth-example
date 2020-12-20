# FastAPI and frontend auth example

This repository is an example for a FastAPI projet with a frontend, demonstrating how auth with an exernal OAuth provider should work. It is associated to the article [Demystifying authentication with FastAPI and a frontend](https://kernelpanic.io/demystifying-authentication-with-fastapi-and-a-frontend) on Kernel Panic.

On this example, it is possible to login with Github OAuth app.

## Getting started

To launch this projet, you may need a PostgreSQL database, that is included in the `docker-compose.yml` file. You can launch it with:

```
$ docker-compose up -d
```

### Backend

To run the backend, you need to create a virtualenv and use [Poetry](https://github.com/python-poetry/poetry) for dependency management:

```
$ virtualenv venv --python=python3.8
$ source venv/bin/activate
$ poetry install
```

Then, you need to set up your Github client id and secret in a `.env` file:

```
GITHUB_CLIENT_ID=<your-client-id>
GITHUB_CLIENT_SECRET=<your-client-secret>
```

And you can launch the backend with:

```
$ uvicorn app.main:app --reload
```

### Frontend

To run the frontend, you need to install the dependencies:

```
$ npm install
```

Then, you can launch it with:

```
$ npm run serve
```

And access it on the [http://localhost:8080](http://localhost:8080) and login !

