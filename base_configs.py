# local or docker-compose -----------------------------------------------
# deploy_method = 'local'
deploy_method = 'docker-compose'

# Database configuration -----------------------------------------------
if deploy_method == 'local':
    database_engine = 'sqlite'
elif deploy_method == 'docker-compose':
    database_engine = 'postgres'

if deploy_method == 'local':
    POSTGRES_HOST = 'localhost'
elif deploy_method == 'docker-compose':
    POSTGRES_HOST = 'db'

POSTGRES_DB_NAME = 'django'
POSTGRES_PORT = 5432
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'psg235a'


# Celery configuration -----------------------------------------------
celery_broker = 'redis'
# celery_broker = 'rabbitmq'

if deploy_method == 'local':
    REDIS_HOST = 'localhost'
    RABBITMQ_HOST = 'localhost'
elif deploy_method == 'docker-compose':
    REDIS_HOST = 'redis'
    RABBITMQ_HOST = 'rabbitmq'

REDIS_PORT = 6379
REDIS_DB = 0

RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'


