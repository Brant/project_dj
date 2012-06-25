#!/usr/bin/python

import os
import shutil


def do_stuff():
    """
    Run a bunch of stuff in sequence
    """
    setup_env()
    initial_syncdb()
    run_server()


def setup_env():
    """
    Run a bunch of stuff to setup the environment
    """
    print "--- Setting up environment ---"
    env = "env"
    my_dir = os.path.abspath( os.path.dirname(__file__) )    
    conf = os.path.join(my_dir, "dj/settings.py")
    conf_template = os.path.join(my_dir, "dj/settings_template.py")
    env_path = os.path.join(my_dir, "env")
    
    commands = ["virtualenv env",
                ". ./env/bin/activate",]
    
    if os.path.isdir(env_path):
        print "--- Environment found, will upgrade packages ---"
        commands.append("pip install --upgrade -r ./requirements.txt")
    else:
        print "--- Did not find environment ---"
        print "--- Will create environment from scratch ---"
        commands.append("pip install -r ./requirements.txt")
    
    
    
    if not os.path.isfile(conf):
        print "--- Did not find settings file ---"
        print "--- Will create settings file base on template ---"
        shutil.copyfile(conf_template, conf)
    
    run_commands(commands)


def initial_syncdb():
    """
    Initial decision making for a fresh environment
    """
    from dj import settings
    if not os.path.isfile(settings.DATABASES["default"]["NAME"]):
        syncdb()


def syncdb():
    """
    Sync the database
    """
    commands = [". ./env/bin/activate",
                "python manage.py syncdb",
                ]
    print "--- Syncing database ---"
    run_commands(commands)
    
    
def run_server():
    """
    Fire up the runserver
    """
    print "--- Running server ---"
    commands = [". ./env/bin/activate",
                "python ./manage.py runserver 8001",
                ]
    run_commands(commands)


def run_commands(commands):
    """
    Just a convinience thing to run commands in succession within a single shell
    """
    os.system(";".join(commands))
    
    
if __name__ == "__main__":
    do_stuff()