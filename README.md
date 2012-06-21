Base Django Project
================

## Get up and running
From the root of this project...

1. **copy:** ./dj/settings_template.py to ./dj/settings.py
2. **in settings.py**, set DEBUG to True (if you are going to start developing stuff)
3. **run:** python ./manage.py syncdb
4. **run:** python ./manage.py runserver 8001

## Customize settings
- Customize *your* settings in ./dj/settings.py
- Customize *global* (commitable, project based) settings in ./dj/conf/*.py 