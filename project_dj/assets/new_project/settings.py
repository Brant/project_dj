"""
Customizable, user settings

Things that need to be customized to fit a particular environment should go here

Should work, out-of-the-box with runserver
"""
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

from project_dj.conf.base import *

# Set DEBUG to False for production use
DEBUG = True

# As you created Django apps for your project, add them here
INSTALLED_APPS += ("website", )

# Media and Static URLs (these are configured to work nicely with runserver
MEDIA_URL = "/media/"
STATIC_URL = '/static/'

from project_dj.conf.append import *
