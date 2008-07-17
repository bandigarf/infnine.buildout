from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='infnine.data',
      version=version,
      description="Infnine Data Types",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Andrija Pr\xc4\x8di\xc4\x87',
      author_email='andrija.prcic@gmail.com',
      url='http://www9.cs.tum.edu',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['infnine'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
