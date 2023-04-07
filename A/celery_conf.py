import os
from celery import Celery
from celery.schedules import crontab
from base_configs import *


if celery_broker == 'redis':
    BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
elif celery_broker == 'rabbitmq':
    BROKER_URL = f"amqp://{RABBITMQ_USER}@{RABBITMQ_HOST}:{RABBITMQ_PORT}//"
    CELERY_RESULT_BACKEND = f"amqp://{RABBITMQ_USER}@{RABBITMQ_HOST}:{RABBITMQ_PORT}//"
else:
    raise ValueError(f"broker {celery_broker} is not supported")

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'ASIA/TEHRAN'


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "A.settings")

celery_app = Celery("A")

celery_app.autodiscover_tasks()
celery_app.conf.broker_url = BROKER_URL
celery_app.conf.result_backend = CELERY_RESULT_BACKEND
celery_app.conf.timezone = CELERY_TIMEZONE

celery_app.config_from_object("django.conf:settings", namespace="CELERY")

celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "add-every-30-seconds": {
        "task": "home.tasks.task1",
        "schedule": 5.0,
        # "args": (1, ),
    },
    "add-every-60-seconds": {
         "task": "home.tasks.task2",
         "schedule": 10.0,
         # "args": (0, ),
    },
}
