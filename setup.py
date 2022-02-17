from setuptools import setup

setup(
    name='bitbucketmanager',
    version='0.0.1',    
    description='Library for managing Bitbucket repositories',
    url='https://github.com/aligent/bitbucketmanager',
    author='John Smith',
    author_email='john.smith@aligent.com.au',
    license='GPL3',
    packages=['bitbucket'],
    install_requires=['requests']
)

