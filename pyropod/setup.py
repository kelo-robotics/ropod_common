#!/usr/bin/env python

from setuptools import setup

setup(name='ropod-common',
      version='2.2.0',
      description='Packages for common ROPOD functionalities',
      author='Argentina Ortega Sainz',
      author_email='argentina.ortega@h-brs.de',
      maintainer='ROPOD',
      packages=['ropod',
                'ropod.pyre_communicator',
                'ropod.pyre_communicator.config',
                'ropod.structs',
                'ropod.utils',
                'ropod.utils.logging',
                ],
      install_requires=['PyYAML>=4.2b1',
                        'pyzmq==17.1.2',
                        'python-dateutil',
                        'pytz',
                        ],
)
