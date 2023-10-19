from setuptools import setup, find_packages

setup(
    name="bank-cli",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'bank=bank_cli.bank_cli:main',
        ],
    },
)