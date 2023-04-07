# django_base

### admin user and password:
root
root

## celery:
> celery -A A worker -l info

> celery -A A beat -l INFO


# postgres
> docker run -d --name postgres -p5432:5432 -e POSTGRES_PASSWORD='psg235a' postgres

> docker exec -it postgres psql -U postgres -c "CREATE DATABASE django"


