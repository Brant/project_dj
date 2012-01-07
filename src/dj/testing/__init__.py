"""
Specific stuff for testing

Basically, this is all just a big hack to allow nose to be the test suite on CI boxes but allow regular django testing to occur elsewhere.
It's all to allow unit testing of abstract base models in both cases, fairly seamlessly

In order to test an abstract class by creating test-only subclasses, 
add a module inside this testing module named something that matches an already-installed BucksAC module

For instance, to add some subclasses to abstract models, you can add 'main' as a module here

Then, you can load your subclasses into a models.py, and load them into your tests elsewhere from there.

This whole mechanism is completely rediculous and a terribly hack. 
It boils down to a bug in the django_nose test suite.

See: https://github.com/jbalogh/django-nose/issues/15 

Note: This module CANNOT be added to pythonpath as a whole.
"""