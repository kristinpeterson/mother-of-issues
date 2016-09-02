try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Python command line tool that creates  \
                    GitHub issues with the same title & body \
                    in multiple repositories.',
    'author': 'kristinpeterson',
    'url': 'http://github.com/kristinpeterson/motherofissues',
    'download_url': 'http://github.com/kristinpeterson/motherofissues',
    'author_email': 'kristinpeterson@me.com',
    'version': '0.0.1',
    'install_requires': ['requests==2.8.1'],
    'packages': ['motherofissues'],
    'name': 'motherofissues'
}

setup(**config)
