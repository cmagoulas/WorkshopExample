from setuptools import setup, find_packages

setup(name='WorkshopExample',
      version='0.0.1',
      description='Random example project for coding workshop',
      url='http://github.com/cmagoulas/WorkshopExample',
      author='Christina Magoulas',
      author_email='christina.magoulas@gmail.com',
      license='MIT',
      install_requires=['numpy'],
      packages=find_packages(exclude=('tests', 'doc', 'data'))
      )
