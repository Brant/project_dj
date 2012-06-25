Base Django Project
================

## 1. Get up and running
From the root of this project...

	python ./gogo.py

## 2. Jump right in
If you want to jump right into designing a homepage, head to:

	./assets/themes/dj/templates/website/home.html

## Structure
It's important to understand a little bit about the structure of the project, as certain areas are "magic" and other areas pertain to the way Django handles it's structure.
### dj
The ./dj directory is essentially where all your settings live. Whenever possible, try to stick to editing ./dj/settings.py instead of anything inside the ./dj/conf directory.

### assets
Assets include:

1. CSS
2. JS
3. Images
4. Templates

### src
The src directory is where the Django apps created by *you* for *your* project should go

### contrib
If there are packages you want to try without necessarily making them part of the requirements.txt file for the virtualenv just yet, stick them in the contrib directory. They will automatically become part of the available python packages in runserver (although you may need to restart the runserver when you add a new package).

## Other puzzle peices
### GoGo
gogo.py is a convinience script designed to get you up and running as fast as possible on a new project

#### GoGo will do a few things for you
1. Setup a virtual environment (using virtualenv)
2. Download and install the packages listed in requirements.txt into the virtual environment
3. Setup a settings file for you, based on a template (if the settings don't already exist)
4. Create and sync the initial database (if it doesnt already exist)
5. Fire up runserver on port 8001

#### You'll need a couple of things beforehand
1. either setuptools or pip
2. virtualenv
3. sqlite3

### Customizing settings
- Customize *your* settings in ./dj/settings.py
- Customize *global* (commitable, project based) settings in ./dj/conf/*.py 

