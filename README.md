# Shop System

## Run Project
Shop system project is very easy to install and deploy in a Docker container.

For running:
```sh
docker-compose up -d --build
```

In project we have 2 apps:

- Users
- Order Processing

The discount system was implemented using Celery Beat.
The task runs every day at midnight and checks if a month has passed since the product creation date.

## Documentation of project

```sh
http://localhost:8080/redoc/
```