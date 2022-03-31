import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version(fname):

    return open(os.path.join(os.path.dirname(__file__), fname)).read().split()[-1]

setup(
    name="eth_client",
    version=get_version(os.path.join('eth_client','version.py')),
    description="simple python client to access ethereum network",
    long_description=read('README.md'),
    author="Ahmad Fahadh Ilyas",
    author_email="fahadhilyas4@gmail.com",
    url="https://github.com/fahadh4ilyas/Simple-Ethereum-Client.git",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities"
    ],
    keywords=["ethereum", "web3", "solidity"],
    requires=[
        "py-solc-x>=1.1.0",
        "web3>=5.20.0"
    ],
    python_requires=">=3.7,<3.11"
)