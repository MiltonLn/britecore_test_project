import json
import os
import sys

from dotenv import load_dotenv

from .utils import get_env_value


ALLOWED_ENVS = ('DEV', 'PROD')
BRITECORE_ENV = os.getenv('BRITECORE_ENV', 'DEV').upper()


# Basic Checks
# ------------------------------------------------------------------------------
assert BRITECORE_ENV in ALLOWED_ENVS, (
    f'BRITECORE_ENV={BRITECORE_ENV} is not one of the allowed values: '
    f'{",".join(ALLOWED_ENVS)}'
)


# Paths
# ------------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_DIR = os.path.dirname(BASE_DIR)
ENV_DIR = os.path.join(BASE_DIR, 'env')
ENV_SECRETS_FILE = os.path.join(ENV_DIR, 'secrets.env')
ENV_SETTINGS_FILE = os.path.join(ENV_DIR, f'{BRITECORE_ENV.lower()}.env')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
FRONTEND_DIR = os.path.join(REPO_DIR, 'frontend')


# Envs
# ------------------------------------------------------------------------------
if os.path.exists(ENV_SECRETS_FILE):
    load_dotenv(dotenv_path=ENV_SECRETS_FILE, override=True)
load_dotenv(dotenv_path=ENV_SETTINGS_FILE, override=True)


# Core Django Settings
# ------------------------------------------------------------------------------
#import pdb; pdb.set_trace()
ALLOWED_HOSTS = get_env_value('ALLOWED_HOSTS', list, os.environ)
SECRET_KEY = get_env_value('SECRET_KEY', str, os.environ)
DEBUG = get_env_value('DEBUG', bool, os.environ)
ENABLE_SENTRY = not DEBUG
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'webpack_loader',
    'django_pdb',

    'risk_types',
    'risks'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR,
            os.path.join(FRONTEND_DIR, 'public')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Database
# ------------------------------------------------------------------------------
POSTGRES_DB = get_env_value('POSTGRES_DB', str, os.environ)
POSTGRES_PORT = get_env_value('POSTGRES_PORT', int, os.environ)
POSTGRES_USER = get_env_value('POSTGRES_USER', str, os.environ)
POSTGRES_PASSWORD = get_env_value('POSTGRES_PASSWORD', str, os.environ)
POSTGRES_HOST = get_env_value('POSTGRES_HOST', str, os.environ)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT
    }
}


# Password validation
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ------------------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(FRONTEND_DIR, "dist"),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')


# Application Settings
# ------------------------------------------------------------------------------

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(FRONTEND_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}