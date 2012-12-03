from .base_settings import *

try:
    from .my_settings import *
except ImportError:
    pass

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    INSTALLED_APPS += ( "debug_toolbar", )
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False, }
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Hack for mediabrute w/ runserver
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