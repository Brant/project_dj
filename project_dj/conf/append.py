"""
Settings to be "appended" to the end of the configuration

These settings usually fall into one of these categories:
    1) override of a previous setting
    2) setting that requires the import of some other specific setting (e.g. DEBUG)

"""
import os
from settings import DEBUG, INSTALLED_APPS, MIDDLEWARE_CLASSES, STATIC_URL, THE_THEME, PROJECT_PATH




# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_PATH + "/assets/" + THE_THEME + "/static/"

os.sys.path.insert(0, os.path.join(PROJECT_PATH, "src"))

# This set of things hacks mediabrute so that the RUNSERVER can serve our static files
# In production, DEBUG should be False, so this will all automatically deactivate
if DEBUG and STATIC_URL.startswith("/") and not STATIC_URL.startswith("//"):
    MEDIABRUTE_CACHE_BASE_URL = "/"
    CSS_DIR = "static/css"
    JS_DIR = "static/js"
    MEDIABRUTE_CSS_URL_PATH = "css"
    MEDIABRUTE_JS_URL_PATH = "js"
    
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        PROJECT_PATH + "/assets/" + THE_THEME + "/static/",
    )
    
    STATIC_ROOT = PROJECT_PATH + "/assets/" + THE_THEME + "/"



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
