from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alpha_tz/__init__.py
from alpha_tz import __version__ as version

setup(
	name="alpha_tz",
	version=version,
	description="App to customize erpnext for Alpha Associates",
	author="KodeIT",
	author_email="smaftah@kodeit.co.tz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
