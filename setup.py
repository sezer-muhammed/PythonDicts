from setuptools import setup, find_packages

setup(
    name='PythonDicts',
    version='0.1.0',
    author='Muhammed Sezer',
    author_email='muhammedsezer12@gmail.com',
    description='A package for handling Python configurations',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
