# Database configuration -----------------------------------------------
# database_engine = 'sqlite'

database_engine = 'postgres'
POSTGRES_HOST = 'localhost'
POSTGRES_DB_NAME = 'django'
POSTGRES_PORT = 5432
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'psg235a'


# Celery configuration -----------------------------------------------
celery_broker = 'redis'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# celery_broker = 'rabbitmq'
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'

