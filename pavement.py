#!/usr/bin/python3

from paver.easy import *
import os
import glob
import shutil
import sys

sys.path.append(os.path.dirname(__file__))

@task
def setup():
    sh('python3 -m pip install -r requirements.txt')

@task
def test():
    sh('python3 -m coverage run --source src -m unittest discover -s test')
    sh('python3 -m coverage html')
    sh('python3 -m coverage report --show-missing')

@task
def clean():
    for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
    for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
    for pycache in glob.glob("*/__pycache__"): shutil.rmtree(pycache)
    for pycache in glob.glob("*/*/__pycache__"): shutil.rmtree(pycache)
    try:
        shutil.rmtree(os.getcwd() + "/cover")
    except:
        pass

@task
def radon():
    sh('radon cc src -a -nb')
    sh('radon cc src -a -nb > radon.report')
    if os.stat("radon.report").st_size != 0:
        raise Exception('radon found complex code')

@task
def run():
    sh('python3 run_guessing_game.py')

@task
@needs(['setup', 'clean', 'test', 'radon'])
def default():
    pass
