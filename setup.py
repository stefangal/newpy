from setuptools import setup
# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
print(this_directory)

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='startnew',
      version='1.3.6',
      author='Stefan Gal',
      author_email='"stefan.mail.sk@gmail.com',
      description='Start new python project with this light cli tool',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/stefangal/newpy',
      packages=['newpy'],
      package_dir={'Newpy': 'newpy'},
      install_requires=required,
      py_modules=['main'],
      entry_points='''
      [console_scripts]
      startnew=main:startnew
    ''',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          'Operating System :: MacOS :: MacOS X',
      ],
      license="mit",
      keywords=['newpy', 'skeleton', 'structure', 'new project', 'template'])
