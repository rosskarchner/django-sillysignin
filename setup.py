import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-sillysignin',
    version=__import__('sillysignin').__version__,
    author='Ross Karchner',
    author_email='ross@karchner.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/rosskarchner/django-sillysignin',
    license='Same license as Python',
    description=u' '.join(__import__('sillysignin').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    zip_safe=False,
    install_requires=['django-class-based-auth-views']
)
