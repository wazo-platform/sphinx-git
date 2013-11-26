from setuptools import setup

from sphinx_git import version


version = version.__version__


setup(
    name='sphinx-git',
    description='git Changelog for Sphinx',
    version=version,
    author='Daniel Watkins',
    author_email='daniel@daniel-watkins.co.uk',
    install_requires=['sphinx', 'GitPython>=0.3.2.RC1'],
    url="https://github.com/OddBloke/sphinx-git",
    packages=['sphinx_git'],
)
