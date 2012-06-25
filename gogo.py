#!/usr/bin/python

import os
import subprocess

def setup_env():    
    os.system("virtualenv env;. ./env/bin/activate; pip install -r ./requirements.txt")
    
    
if __name__ == "__main__":
    setup_env()