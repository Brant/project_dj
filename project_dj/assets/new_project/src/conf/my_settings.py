"""
Customizable, user settings

Things that need to be customized to fit a particular environment should go here

Should work, out-of-the-box with runserver
"""
import os

# Set DEBUG to False for production use
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database settings
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': '',                      # Or path to database file if using sqlite3.
#        'USER': '',                      # Not used with sqlite3.
#        'PASSWORD': '',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
#}


# Media and Static URLs (these are configured to work nicely with runserver
#MEDIA_URL = "/media/"
#STATIC_URL = '/static/'

# Email server stuff
#    EMAIL_HOST = ''
#    EMAIL_HOST_USER = ''
#    EMAIL_HOST_PASSWORD = ''

