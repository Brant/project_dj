"""
Customizable, user settings

Things that need to be customized to fit a particular environment should go here

Should work, out-of-the-box with runserver
"""

from conf.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJECT_PATH + '/dj.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_URL = "/media/"
STATIC_URL = '/static/'

from conf.append import *

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    INSTALLED_APPS += ( "debug_toolbar", )
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )