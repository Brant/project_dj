"""
Testing plugin for django_nose
"""
import sys

from django_nose.plugin import DjangoSetUpPlugin


class HackedDjangoSetUpPlugin(DjangoSetUpPlugin):
    """
    Hacked DjangoSetUpPlugin
    """
    def begin(self):
        """
        Overridden to add 'TEST_INSTALLED_APPS' to app list when using suite
        """
        sys_stdout = sys.stdout
        sys.stdout = self.sys_stdout

        from django.conf import settings
        settings.INSTALLED_APPS += getattr(settings, 'TEST_INSTALLED_APPS',  [])

        self.runner.setup_test_environment()
        self.old_names = self.runner.setup_databases()
