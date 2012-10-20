"""
Customizable, user settings

Things that need to be customized to fit a particular environment should go here

Should work, out-of-the-box with runserver
"""
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
os.sys.path.insert(0, os.path.join(PROJECT_PATH, "src"))

from project_dj.conf.base import *

# Set DEBUG to False for production use
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database settings
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

# As you created Django apps for your project, add them here
INSTALLED_APPS += ("website", )

# Media and Static URLs (these are configured to work nicely with runserver
MEDIA_URL = "/media/"
STATIC_URL = '/static/'

from project_dj.conf.append import *

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    INSTALLED_APPS += ( "debug_toolbar", )
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False, }
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''

#NOODLES_EMAIL_LIST = []
#EMAIL_SUBJECT_PREFIX = ""    
#DEFAULT_FROM_EMAIL = ''
#SERVER_EMAIL = ''