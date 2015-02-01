from distutils.core import setup

setup(
    author='William Cember',
    author_email='wcember@gmail.com',
    description='Python package to compile hex into Script (bitcoin scripting language)',
    keywords=['bitcoin', 'compiler'],
    name='bithex',
    packages=['bithex',],
    license='MIT',
    long_description=open('README.txt').read(),
    url='https://github.com/wcember/bithex',
    version='0.1',
)