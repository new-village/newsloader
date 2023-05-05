''' setup.py
'''
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='nsloader',
    version='1.1.0',
    author='new-village',
    url='https://github.com/new-village/nsloader',
    description='This script collects articles from Wall Street Journal and returns it in dict format.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['playwright'],
    packages=find_packages(),
    package_data={'': ['config/*.json']},
)