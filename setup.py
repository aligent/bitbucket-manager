from setuptools import setup

setup(
    name='bitbucketmanager',
    version='0.0.1',    
    description='Library and CLI tool for managing Bitbucket repositories',
    url='https://github.com/aligent/bitbucketmanager',
    author='John Smith',
    author_email='john.smith@aligent.com.au',
    scripts=['bin/bitbucket'],
    license='GPL3',
    packages=['bitbucket'],
    install_requires=['requests']
)

