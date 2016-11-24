#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2016 IBM Corporation

Licensed under the Apache License, Version 2.0 (the “License”);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an “AS IS” BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

	Contributors:
		* Rafael Sene <rpsene@br.ibm.com>
"""

from setuptools import setup, find_packages
import time

with open('README.rst') as f:
	readme = f.read()

with open('LICENSE') as f:
	toollicense = f.read()

setup(
	name='sca',
	version='1.0.timestamp',
	description='Source Code Advisor highlight potential problems in your source code and offer suggested solutions.',
	long_description=readme,
	author='Rafael Peria de Sene',
	author_email='rpsene@br.ibm.com',
	url='https://www-304.ibm.com/webapp/set2/sas/f/lopdiags/sdklop.html',
	license=toollicense,
	packages=find_packages(exclude=("tests",)),
	data_files=[("", ["LICENSE"])],
	include_package_data=True,
	test_suite='nose.collector',
	tests_require=['nose'],
	scripts=['bin/sca'],
	zip_safe=False,
	classifiers=[
		'Development Status :: 1 - Planning',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: C',
		'Programming Language :: C++',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: Apache Software License',
          ],
)
