"""
Django settings for test_app_1 project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.conf.global_settings import STATICFILES_FINDERS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_NAME = 'test_app_1'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oy(b*-nyb*&u3!w#-ecp*2%w#^(cijdcjixq*i#7aiscr2hujm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'apps.users',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'custom_user',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'sorl.thumbnail',
    'compressor',

    # project apps list
    # 'apps.foo.apps.FooConfig',
    # 'apps.bar.apps.BarConfig',
]

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_SIGNUP_FORM_CLASS = 'apps.users.forms.CustomSignupForm'
ACCOUNT_FORMS = {'login': 'apps.users.forms.CustomSignInForm'}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_app_1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'test_app_1.context_processors.head_body_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'test_app_1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# LANGUAGES = (
#     ('ru', 'Russian'),
#     ('ua', 'Ukrainian'),
#     ('en', 'English'),
# )
#
# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# ))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

PUBLIC_ROOT = os.path.join(BASE_DIR, '../', 'public')
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)


COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    # ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
    # ('text/x-scss', 'sass --style compressed {infile} {outfile}'),
)
