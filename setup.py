
from setuptools import setup, find_packages

setup(
    name='fake_profile',
    version='0.1.0',
    author='Collins O. Odhiambo',
    description = "This is a python package that helps developers to generate fake social media user profiles and interactions for development purposes",
    author_email='comon928@gmail.com',
    url='https://github.com/C-o-m-o-n/fake_profile',
    packages=find_packages(),
    install_requires=[
        'Faker',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


