from distutils.core import setup

setup(name='performotron',
      version='0.1',
      py_modules=['performotron'],
      author='Isaac Laughlin',
      author_email='isaac.laughlin@galvanize.com',
      url='',
      install_requires=['sklearn', 'pyyaml', 'requests'],
      tests_requires = ['nose']          
)
      
      
