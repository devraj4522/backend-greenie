import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("backend_greenie")

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()






# import os,ssl, platform
# from celery import Celery
# from celery.schedules import crontab

# ## Get the base REDIS URL, default to redis' default
# BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')




# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object("django.conf:settings", namespace="CELERY")

# # #celery_beat settings
# # app.conf.beat_schedule = {
# #     'do-task-everyday-at-8':{
# #         'task': 'distributors.tasks.sleepy',
# #         'schedule': crontab(hour=9,minute=45),
# #         'args': (7,20)
# #     }
# # }
# #celery_beat settings
# app.conf.beat_schedule = {
#     'do-task-everyday-at-8':{
#         'task': 'distributors.tasks.send_automated_repayment_mails',
#         'schedule': crontab(hour=8,minute=11),
#     }
# }

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

# app.conf.broker_url = BASE_REDIS_URL

# # this allows you to schedule items in the Django admin.
# app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'


