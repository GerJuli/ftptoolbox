# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='ftptools',
    version='0.0.1',
    description='Toolbox for FTP operations',
    long_description='Toolbox for backups and sync of files and directories',
    author='Julian-Samuel Gebuehr',
    author_email='julian-samuel@gebuehr.net',
    url='https://github.com/translationalneurosurgery/ftptools.git',
    download_url='https://github.com/translationalneurosurgery/ftptools.git',
    license='MIT',
    packages=['backup', 'sync_file'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Advanced user',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        ]
)
