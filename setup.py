from distutils.core import setup

setup(
    name='Cascading Options',
    version='0.1.0',
    author='Jonathan Marini',
    author_email='j.marini@ieee.org',
    scripts=['cascading_options.py',],
    install_requires=[
        'PyYAML == 3.10',
    ],
)
