from setuptools import setup, find_packages

setup(
    name='GeneralTools',
    version='0.1',
    author='Nima Dehghani, MIT @neurovium',
    description='A collection of general utility tools inspired by DrWatson.jl',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here, if any
        # For example: 'numpy>=1.15.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
