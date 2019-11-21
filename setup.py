# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('docs/README.rst') as readme_file:
    readme = readme_file.read()

with open('docs/HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Greg Anuzelli",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="An unofficial Cisco Mobility Express Python API.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ciscomeapi',
    name='ciscomeapi',
    packages=find_packages(include=['ciscomeapi']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/anuzellig/cisco-mobility-express-python-api',
    version='0.1',
    zip_safe=False,
)