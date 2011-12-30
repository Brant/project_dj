TEST_APPS = ("django_nose", )

#TEST_INSTALLED_APPS = ("testing.main", )

#TEST_RUNNER = "testing.runner.HackedNoseTestSuiteRunner"
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ["--with-xcoverage", "--cover-inclusive", "--with-xunit", "--exe", "--verbosity=3"]
NOSE_PLUGINS = [
    'nosexcover.XCoverage',
    "nose_exclude.NoseExclude"
]