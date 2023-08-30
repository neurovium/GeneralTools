from setuptools import setup, find_packages

# setup(
#     name='GeneralTools',
#     version='0.1',
#     packages=['.'],
# )
with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name='prjtools',
    version='0.1',
    author='Nima Dehghani, MIT @neurovium',
    description='A collection of general utility tools',
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    # long_description_content_type="text/markdown"
    install_requires=[
        # List your project dependencies here, if any
        # For example: 'numpy>=1.15.0',
    ],
    extras_require={
        # "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    python_requires = '>=3.10',
)
