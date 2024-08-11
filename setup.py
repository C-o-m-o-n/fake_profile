from setuptools import setup, find_packages

setup(
    name='fake_profile',
    version='0.1.0',
    description='A package to generate fake social media user data and interactions',
    author='Collins O. Odhiambo',
    author_email='your.email@example.com',
    url='https://github.com/C-o-m-o-n/fake_profile',
    packages=find_packages(),
    install_requires=[
        'Faker',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

