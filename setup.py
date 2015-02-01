from distutils.core import setup

setup(
    name='epub',
    version='0.1',
    packages=['epub',],
    package_data={'epub': ['epub_templates/*',]},
    license='',
    long_description=open('README.txt').read(),
)