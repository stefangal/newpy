from setuptools import setup

setup(name='newpy',
      version='0.1.0',
      author='Stefan Gal',
      author_email='"stefan.mail.sk@gmail.com',
      description='Start project with this light tool',
      url='https://github.com/stefangal/newpy',
      packages=['newpy'],
      package_dir={'Newpy': 'newpy'},
      install_requires=['Click'],
      py_modules=['main'],
      entry_points='''
      [console_scripts]
      startnew=main:run
    ''',
      license="mit",
      keywords=['newpy', 'skeleton', 'structure', 'new project', 'template'])
