from setuptools import setup, find_packages
import sys
setup(name='ziggurat_foundations',
      version='0.2',
      description=""" Set of classes that are reusable across various types of
      web apps, base user object, auth relationships + structured resource tree
      """,
      author='Marcin Lulek',
      author_email='info@webreactor.eu',
      license='BSD',
      packages=find_packages(),
      test_suite='ziggurat_foundations.tests',
      install_requires=["sqlalchemy", "cryptacular", 'webhelpers']
      )