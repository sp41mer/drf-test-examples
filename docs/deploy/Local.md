# Local deployment
Local deployment

## Set up environment
`pip install -r requirements.txt`

## Run tests
`python manage.py test`

## Run migrations
`python manage.py migrate`

## Create superuser
`python manage.py createsuperuser`

## Local settings guide
DATABASES: allows to start local environment without PostgresSQL server
LOGGING: shows all DB queries
DRF_HTML_RENDERER_ENABLED: enable to expore API via DRF interface

## Run server
`python manage.py runserver`

## Docker-Compose
`docker-compose up`