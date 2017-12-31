from setuptools import setup
from setuptools import find_packages

setup(
    name='shogiwars_kifu',
    version='1.0.0',
    packages=find_packages(),
    description='kifu downloader from shogiwars',
    author='Keisuke Fukuta',
    author_email='fukuta6140@gmail.com',
    url='https://github.com/fukuta0614/shogiwars_kifu',
    install_requires=open('requirements.txt').readlines(),
    license='MIT',
    keywords='utility',
    entry_points={'console_scripts': ['shogiwars_kifu=shogiwars_kifu:main']},
)
