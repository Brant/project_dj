from setuptools import setup, find_packages

setup(
    name = "project_dj",
    version = "0.4",
    url = 'https://github.com/Brant/project_dj',
    license = 'GPL',
    description = "Spins up starter django projects",
    long_description = open('README.md').read(),

    author = 'Brant Steen',
    author_email = 'brant.steen@gmail.com',

    packages = find_packages(exclude=('tests', )),
    include_package_data = True,
    zip_safe = False,

    install_requires = ['setuptools', 'django', ],

    scripts = ["scripts/project_dj", ],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
