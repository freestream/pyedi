import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

tests_require = [
    'pytest'
]

setuptools.setup(
    name='pyedi',
    version='1.0.0',
    author='Anton Samuelsson',
    author_email='samuelsson.anton@gmail.com',
    description='A lightweight EDI file parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/freestream/pyedi',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    tests_require=tests_require,
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
)
