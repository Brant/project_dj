"""
Settings to be "appended" to the end of the configuration

These settings usually fall into one of these categories:
    1) override of a previous setting
    2) setting that requires the import of some other specific setting (e.g. DEBUG)

"""
from dj.settings import DEBUG, INSTALLED_APPS, MIDDLEWARE_CLASSES, STATIC_URL, THE_THEME, PROJECT_PATH

JS_SETTINGS_TEMPLATE = "mediabrute/js/config.txt"

CSS_TOP_FILES = ["base.css", "style.css", ]
CSS_BOTTOM_FILES = []


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
