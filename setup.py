from setuptools import setup
setup(
	name="MCME API",
	version="0.1",
	packages=['mcmeAPI'],
	include_package_data=True,
	zip_safe=False,
	install_requires=['Flask', 'sqlalchemy']
	)