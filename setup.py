from distutils.core import setup

setup(
    name='Cascading Options',
    version='0.1.0',
    url='http://github.com/jmarini/cascading-options',
    author='Jonathan Marini',
    author_email='j.marini@ieee.org',
    license='MIT',
    py_modules=['cascading_options',],
    install_requires=[
        'PyYAML == 3.10',
    ],
)
