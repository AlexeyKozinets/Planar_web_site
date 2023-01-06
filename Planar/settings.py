"""
Django settings for Planar project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path                                #    multiLang: source) https://www.youtube.com/watch?v=F0O0LLz12BU&list=LL&index=3
import os                                               #    multiLang:0) pip install django-modeltranslation
from django.utils.translation import gettext_lazy as _  # <- multiLang:1) import for language list (next: settings.py)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o=epjjb#f7w4lho(wc7ce8jlmn64s-8*!#=@f-e63-k@adsu6^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'modeltranslation',                                 # <- multiLang:2) plug in "modeltranslation" app (next: settings.py)

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    'ckeditor_uploader',

    'main_site',
    'users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',        # <- multiLang:3) enables language selection based on data from the 
                                                        # request (must be between:
    'django.middleware.common.CommonMiddleware',        # 'django.contrib.sessions.middleware.SessionMiddleware' and
    'django.middleware.csrf.CsrfViewMiddleware',        # 'django.middleware.common.CommonMiddleware') (next: settings.py)
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Planar.urls'

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
        },
    },
]

# WSGI_APPLICATION = 'Planar.wsgi.application' # !!!!home work


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'                            # <-- for admin and translation (if ru then lang in "locales" must be en)
                                                # and translated text must be ru

LANGUAGES = [                                   # <- multiLang:4) language list (next: settings.py)
    ('ru', _('Russian')),
    ('en', _('English')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'        # <- multiLang:5) language which will use in default (next: settings.py)
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'    # <- multiLang:6) language which will use by slug in default;

LOCALE_PATHS = (                                # also need create a folder in base directory where translation will save
    os.path.join(BASE_DIR, 'locale'),           # (next: settings.py);
)


TRANSLATABLE_MODEL_MODULES = ["main_site.models", ]

TIME_ZONE = 'UTC'

USE_I18N = True                                 # <- multiLang:7) must be equal "True" (next: create *app_name*/translation.py)

USE_TZ = True


AUTH_USER_MODEL = 'users.CustomUser'            # user!!!!!!!!!!!


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]


MEDIA_URL = 'media/'                            ####?
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    ####? read more info about


CKEDITOR_UPLOAD_PATH = "uploads/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom':[
            [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', ],
            [ 'NumberedList', 'BulletedList','-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'Outdent', 'Indent',],
            [ 'Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            [ 'Maximize', 'ShowBlocks' ],
            [ 'Link', 'Unlink', ],
            [ 'Maximize', 'ShowBlocks' ],
            [ 'Styles', 'Format', 'Font', 'FontSize' ],
            ['Source',],
        ],
        'width': 'full', # + .django-ckeditor-widget{width: 100%;}
    },
}