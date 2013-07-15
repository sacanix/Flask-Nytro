"""
Flask-Nytro
-------------

Nytro is an extension to help developer providing a set of useful tools
giving even more facility to development apps with Flask.
"""
from setuptools import setup


setup(
    name='Flask-Nytro',
    version='1.0',
    url='http://example.com/flask-nytro/',
    license='BSD',
    author='Tony Kamillo (Sacanix)',
    author_email='tonysacanix@gmail.com',
    description='''Nytro is an extension to help developer providing a set of useful tools
    giving even more facility to development apps with Flask.''',
    long_description=__doc__,
    #py_modules=['flask_sqlite3'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flask_nytro'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)