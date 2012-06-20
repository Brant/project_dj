TEST_APPS = ("django_nose", )

#TEST_INSTALLED_APPS = ("testing.main", )
TEST_INSTALLED_APPS = ("noodles.testing", )

TEST_RUNNER = 'dj.testing.runner.HackedNoseTestSuiteRunner'

NOSE_ARGS = ["--with-xcoverage", "--cover-inclusive", "--with-xunit", "--exe", "--verbosity=3"]
NOSE_PLUGINS = [
    'nosexcover.XCoverage',
    "nose_exclude.NoseExclude"
]