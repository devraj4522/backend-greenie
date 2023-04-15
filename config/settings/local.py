from .base import *  # noqa
from .base import env
import os

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="r3HF4UBjkXb4367pGwq9G8IF7PnbagZO9xGYhpXe6QVJD6qmzMZ8wsM1OvN1AlGI",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "backend-greenie-production-efac.up.railway.app"]


RAILWAYS_EXTERNAL_HOSTNAME = os.environ.get('RAILWAYS_EXTERNAL_HOSTNAME')
if RAILWAYS_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RAILWAYS_EXTERNAL_HOSTNAME)
    ALLOWED_HOSTS.append('https://backend-greenie.onrender.com')
CSRF_TRUSTED_ORIGINS = ["https://backend-greenie-production-efac.up.railway.app", f"https://{os.environ.get('RAILWAYS_EXTERNAL_HOSTNAME')}", "https://backend-greenie.onrender.com"]
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405


# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]


# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405
# Celery
# ------------------------------------------------------------------------------
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-always-eager
CELERY_TASK_ALWAYS_EAGER = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True
# Your stuff...
# ------------------------------------------------------------------------------
CELERY_BROKER_URL = env("REDIS_URL", default="redis://127.0.0.1:6379")
CELERY_RESULT_BACKEND = env("REDIS_URL", default="redis://127.0.0.1:6379")
CELERY_TASK_ROUTES = {
 '*.tasks.*': {'queue': os.getenv('CELERY_QUEUE_NAME')},
}
CELERY_TASK_CREATE_MISSING_QUEUES = 1
CELERY_WORKER_MAX_TASKS_PER_CHILD = 500
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
CELERY_ACKS_LATE = True
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
