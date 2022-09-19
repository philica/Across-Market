from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in across_marketplace/__init__.py
from across_marketplace import __version__ as version

setup(
	name="across_marketplace",
	version=version,
	description="market place for farmers",
	author="fikremariam getu",
	author_email="fikretucker79@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
