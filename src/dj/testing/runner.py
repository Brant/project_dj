"""
Custom Test Runner
"""
from django_nose.runner import NoseTestSuiteRunner, _get_plugins_from_settings
from django_nose.plugin import ResultPlugin

from nose.core import TestProgram

from dj.testing.plugin import HackedDjangoSetUpPlugin

class HackedNoseTestSuiteRunner(NoseTestSuiteRunner):
    """
    Hacked suite runner based on NoseTestSuiteRunner
    """
    def run_suite(self, nose_argv):
        """
        Override to load up hacked DjangoSetUpPlugin
        """
        result_plugin = ResultPlugin()
        plugins_to_add = [HackedDjangoSetUpPlugin(self), result_plugin]

        for plugin in _get_plugins_from_settings():
            plugins_to_add.append(plugin)

        TestProgram(argv=nose_argv, exit=False, addplugins=plugins_to_add)
        return result_plugin.result
