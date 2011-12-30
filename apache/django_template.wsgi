import os
import sys

from django.core.handlers.wsgi import WSGIHandler
sys.path = ['/home/brant/webapps/django/sites/<project_name>', '/home/brant/webapps/django/sites/<project_name>/src'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'dj.settings'
application = WSGIHandler()
