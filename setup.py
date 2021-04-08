from setuptools import setup, find_packages
from os.path import join, dirname
import telegramlogger

setup(
    name='telegramlogger',
    version=telegramlogger.__version__,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
    'console_scripts': []
    }
)
