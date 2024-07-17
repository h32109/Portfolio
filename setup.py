import os
import sys
import re

from setuptools import setup
from setuptools import find_packages

ROOT = os.path.dirname(os.path.abspath(__file__))
VERSION_CMP = r'<|<=|!=|==|>=|>|~=|==='

sys.path.insert(0, os.path.join(ROOT, ""))

about = {}
with open(os.path.join(ROOT, 'portfolio', '__about__.py')) as f:
    exec(f.read(), about)  # nosec: about file is benign


# version info
VERSION = about["__version__"]

# organization info
ORG = about["__organization__"]

# solution name
SOLUTION_NAME = about["__solution_name__"]

# read requirements files
with open('requirements.txt') as f:
    install_requirements = f.read().splitlines()

# read test requirements files
with open('requirements-test.txt') as f:
    test_requirements = f.read().splitlines()


def parse_dependency_links(requirements):

    private_requirements = []
    for requirement in requirements:
        package_info = re.split(VERSION_CMP, requirement)
    return private_requirements


setup(
    name=SOLUTION_NAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=install_requirements,
    extras_require={
      "test": test_requirements
    },
    entry_points={
        'console_scripts': [
            'portfolio = portfolio.main:main'
        ]
    },
    classifiers=[
        'Framework :: FastAPI',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3.11',
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        'Topic :: Search'

    ]
)