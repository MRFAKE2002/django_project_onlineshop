"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
# from environs import Env 
import os

# # For environment variable
# env = Env()
# env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env("DJANGO_SECRET_KEY")
SECRET_KEY = "django-insecure-b764$#(&o4o((cvy!z^nsseq5@erq#e^0%5r5a(%c24*f^*sde"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env.bool("DJANGO_DEBUG")
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    # Django apps
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps 
    
    'allauth', # We use this app to make our login and logout and signup for our project.
    'allauth.account',
    'crispy_forms', # We use this app for make our forms better in templates.
    'rosetta', # We use this app to translate our codes to persian and we should make our LANGUAGES in config settings.
    
    # My apps 
    
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'product.apps.ProductConfig',
    'cart.apps.CartConfig',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# locale

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'fa'

LANGUAGES = (
    ('en', 'English'),
    ('fa', 'Persian'),
)

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tehran'

USE_I18N = True     # Internationalization
USE_L10N = True     # Localization
USE_TZ = True

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, "locale"),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIR = os.path.join(STATIC_URL, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy forms for config

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Accounts CustomUser config 

AUTH_USER_MODEL = 'accounts.CustomUser' 

# Login and Logout redirect config

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

# Allauth config

ACCOUNT_SESSION_REMEMBER = True     # Save user information

# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False 

ACCOUNT_AUTHENTICATION_METHOD = 'email'     # User login with email

# ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

# For send a email confirmation to console

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# # For send a confirmation from our email to user email

# EMAIL_PACKED = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "mr3fake@gmail.com"
# EMAIL_HOST_PASSWORD = "roozbehbadali1381"
