from setuptools import setup

setup(name='newpy',
      version='0.2.0',
      author='Stefan Gal',
      author_email='"stefan.mail.sk@gmail.com',
      description='Start new python project with this light cli tool',
      url='https://github.com/stefangal/newpy',
      packages=['newpy'],
      package_dir={'Newpy': 'newpy'},
      install_requires=['Click'],
      py_modules=['main'],
      entry_points='''
      [console_scripts]
      startnew=main:startnew
    ''',
      license="mit",
      keywords=['newpy', 'skeleton', 'structure', 'new project', 'template'])
