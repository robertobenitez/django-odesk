import os
from setuptools import setup, find_packages

version = __import__('django_odesk').get_version()

readme = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
README = readme.read()
readme.close()

setup(name='django-odesk',
      version=version,
      description='oDesk API integration for Django',
      long_description=README,
      author='Oleksiy Solyanyk',
      author_email='solex@odesk.com',
      install_requires = ['python-odesk>=0.4.1', ],
      packages = find_packages(),
      classifiers=['Development Status :: 1 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities',],)
