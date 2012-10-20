


TEST_APPS = ("django_nose", )

TEST_RUNNER = "django_nose.runner.NoseTestSuiteRunner"

NOSE_ARGS = ["--with-xcoverage", "--cover-inclusive", "--with-xunit", "--exe", "--verbosity=3"]
NOSE_PLUGINS = [
    'nosexcover.XCoverage',
    "nose_exclude.NoseExclude"
]