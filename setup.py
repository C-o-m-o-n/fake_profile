import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

DESCRIPTION = 'This is a python package that helps developers to generate fake social media user profiles and interactions for development purposes'

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setup(
    name='fake_profile',
    version='0.3.0',
    author='Collins O. Odhiambo',
    description = DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
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


