from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in legal_app/__init__.py
from legal_app import __version__ as version

setup(
    name="legal_app",
    version=version,
    description="A comprehensive legal management application",
    author="Your Company",
    author_email="legal@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
