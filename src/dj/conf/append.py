"""
Settings to be "appended" to the end of the configuration

These settings usually fall into one of these categories:
    1) override of a previous setting
    2) setting that requires the import of some other specific setting (e.g. DEBUG)

"""
from dj.settings import DEBUG, INSTALLED_APPS, MIDDLEWARE_CLASSES, STATIC_URL, THE_THEME, PROJECT_PATH

if STATIC_URL.startswith("/") and not STATIC_URL.startswith("//"):
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
