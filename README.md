Base Django Project
================

## Get up and running
From the root of this project...

	python ./gogo.py

### That will do a few things for you
1. Setup a virtual environment (using virtualenv)
2. Download and install the packages listed in requirements.txt into the virtual environment
3. Setup a settings file for you, based on a template (if the settings don't already exist)
4. Create and sync the initial database (if it doesnt already exist)
5. Fire up runserver on port 8001

### You'll need a couple of things beforehand
1. either setuptools or pip
2. virtualenv
3. sqlite3

## Jump right in
If you want to jump right into designing a homepage, head to:

	./assets/themes/dj/templates/website/home.html


## Customize settings
- Customize *your* settings in ./dj/settings.py
- Customize *global* (commitable, project based) settings in ./dj/conf/*.py 

