Project DJ (A base Django project)
================
This is my codebase for getting started with a new Django project. It's designed to smooth a lot of rough edges, mostly regarding things like configurations that can be confusing and/or time consuming.

Project DJ takes a [convention over configuration](http://en.wikipedia.org/wiki/Convention_over_configuration) approach to starting a Django project. In other words, there's a lot of stuff that the basic *django-admin startproject* doesn't include that I always need to then fiddle with settings to add. For example, remember that time that you made a django project but didn't use the Admin panel? Yea, me either. That's why Project DJ just adds it to your project by default. 

It also provides some handy front-end stuff for websites that I almost always use.

This is really designed to help you start your *own* project, which will presumably be under its own version control.

## Jump right in
Just run a few commands, and Project DJ will set you up with a django project structure.

### 0. Beforehand
You'll need a couple of things installed first

1. Python 2.7.x
2. [virtualenv](https://pypi.python.org/pypi/virtualenv)
3. git
4. sqlite3

### 1. Get up and running
You don't even need to download this module directly! 

From a directory where you want to start your project, run these commands:

	virtualenv env --system-site-packages
	. ./env/bin/activate
	pip install git+git://github.com/Brant/project_dj.git
	project_dj <your_project> ./
	pip install -r requirements.txt
	python manage.py syncdb
	python manage.py runserver 8001
 
### 2. Start working
If you want to start creating Django apps for your project, they should live here:

	./<your_project>/<your_app>

There's one there for you already, named *website*. You can feel free to start with that one.

If you want to jump right into designing a homepage, head to:

	./assets/themes/dj/templates/website/home.html
	
## Structure
It's important to understand a little bit about the structure of the project, as certain areas are "magic" and other areas pertain to the way Django handles it's structure.

### \<your_project\>
The \<your_project\> directory is where the Django apps created by *you* for *your* project should go

### assets
Assets include:

1. CSS
2. JS
3. Images
4. Templates

### env
The env directory is the default place that virtualenv will setup your isolated python environment for this project. If you want to change the directory name, you can do so in gogo.py.

### dev
This is a directory to fill with things useful for external tools. For example, a template of apache settings, an RC file for pylinting, etc.
