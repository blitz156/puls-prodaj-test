from .installed_apps import *
import dj_database_url
import logging
import os

SECRET_KEY = "dkf)^fdo5_xenbz)z1jw69i0cew98oo18z3o-pzm$2^_8aalr#"

ANONYMOUS_USER_ID = -1
SITE_ID = 1
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

##################################################################
# Debug settings
##################################################################

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

##################################################################
# Databases settings (for docker)
##################################################################

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL', 'postgres://postgres@db/postgres'), conn_max_age=600),
}

##################################################################
# Logging settings
##################################################################

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'

LOG_FORMATTER = logging.Formatter(
    u'%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
    datefmt=LOG_DATE_FORMAT)

CONSOLE_HANDLER = logging.StreamHandler()

CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)

CONSOLE_HANDLER.setLevel(logging.DEBUG)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'raven_error': {
            'level': 'ERROR',
            'handlers': [],
            'propagate': False,
        },
    }
}

##################################################################
# Assets settings
##################################################################

from os.path import dirname, basename, join

SETTINGS_PATH = dirname(__file__)
PROJECT_PATH = dirname(SETTINGS_PATH)
PROJECT_NAME = basename(PROJECT_PATH)
SERVER_PATH = dirname(PROJECT_PATH)
ROOT_PATH = dirname(SERVER_PATH)

FILE_UPLOAD_PERMISSIONS = 0o644

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL
MEDIA_ROOT = join(SERVER_PATH, 'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = ('static',)

##################################################################
# Finders, loaders, middleware and context processors
##################################################################

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    },
]

MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

if DEBUG:
    def show_toolbar(request):
        return True

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }
    MIDDLEWARE = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE
    INSTALLED_APPS += ('debug_toolbar', )


CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [

]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'MAX_ENTRIES': 10000,
        },
    }
}

##################################################################
# REST framework settings
##################################################################

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

if DEBUG:
    del REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES']