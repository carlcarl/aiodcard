from setuptools import setup
from setuptools import find_packages

import re
import os


def get_release():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    root = os.path.dirname(__file__)
    init_py = os.path.join(root, 'aiodcard', '__init__.py')
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            raise RuntimeError('Cannot find version in aiodcard/__init__.py')


setup(
    name='aiodcard',
    description='Dcard crawler using asyncio(coroutine)',
    long_description=open('README.rst').read(),
    version=get_release(),
    author='carlcarl',
    author_email='carlcarlking@gmail.com',
    url='https://github.com/carlcarl/aiodcard',
    packages=find_packages(),
    license='MIT',
    package_data={
    },
    entry_points={
    },
    keywords=['dcard', 'crawler', 'coroutine'],

    classifiers=[
        'Development Status :: 4 - Beta'
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
    ],
)
