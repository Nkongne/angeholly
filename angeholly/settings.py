"""
Django settings for angeholly project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from django.utils.translation import ugettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^ps#l1!&(g6tqfu2nda26l^n1r!x+28)6$f#@6m)h+en%7^h-j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STRIPE_PUB_KEY = 'pk_test_51Igjh5COYGHkJKs11TGd0VGWKGrTklhXX98Eb0p2EGMCEqNc4V1S7YH34n3wLgkdW8jQj8joopmobEez2GsQEHkO00m2DjyenW'
STRIPE_SECRET_KEY = 'sk_test_51Igjh5COYGHkJKs1yTXlCcrvhL5Jbkpnl y0BeZfYRsWMeuiCCeIq4p9WnVedsSNNnV2i7fPefW8HJGwQr94uOS5J00eB6dXXnS'

# Application definition
LOGIN_URL='login'
LOGIN_REDIRECT_URL='vendor_admin'
LOGOUT_REDIRECT_URL='frontpage'


SESSION_COOKIE_AGE=86400
CART_SESSION_ID='cart'



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.cart',
    'apps.shop',
    'apps.vendors',
    'apps.orders',
    'apps.product'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'angeholly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.product.context_processors.menu_categories',
                'apps.cart.context_processors.cart'
            ],
        },
    },
]
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.i18n',)
WSGI_APPLICATION = 'angeholly.wsgi.application'
LOCALE_PATHS=(os.path.join(BASE_DIR, "locale"),)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'angeholly',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'bd',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


LANGUAGES = [ # Available languages
        ('en', _("English")),
        ('de', _("German")),
        ('fr', _("French")),
    ]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'

MEDIA_URL='/media/'
MEDIA_ROOT= BASE_DIR / 'media/'


TWILIO_ACCOUNT_SID = 'ACe32013ee79c2ab915dc4146bc54dbced'
TWILIO_AUTH_TOKEN = '98314715f8753fe04e2641e1d7627756'

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nkongnedev@gmail.com'
EMAIL_HOST_PASSWORD = 'mercidieu25mai1992'