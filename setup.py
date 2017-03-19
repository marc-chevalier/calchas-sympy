#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='calchas_sympy',
    version='0.8',
    description='A sympy plugin for Calchas',
    url='https://github.com/ProjetPP',
    author='Projet Pensées Profondes',
    author_email='marc.chevalier@ens-lyon.org',
    license='MIT',
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'calchas_datamodel',
        'sympy >= 1.0',
    ],
    packages=[
        'calchas_sympy',
    ],
)
