from _install_hook import _InstallCommand
from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.

setup(
    cmdclass={'install': _InstallCommand},
    name="Authlib",
    install_requires=[
        "cryptography>=3.2",
    ],
)
