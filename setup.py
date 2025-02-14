from setuptools import setup, find_packages
setup(
    name="binaryTREE_operations",
    version="0.2",
    packages=find_packages(),
    description="A package for binary tree operations",
    author="Amir",
    author_email="amirsakib16@gmail.com",
    license="MIT",
    entry_points={
    "console_scripts": [
        "binaryTREE_operations = binaryTREE_operations.main:main",
    ]
}

)