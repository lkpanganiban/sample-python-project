from setuptools import setup, find_packages

setup(
    name="sample-python-cli",
    version="0.1",
    author="Ian Panganiban",
    author_email="ian.panganiban@gmail.com",
    description=("A sample python calculator."),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'samplepycli=sample_python_calculator.run:main'
        ]
    },
    install_requires=[
        'fire'
    ],
)

