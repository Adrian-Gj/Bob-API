from distutils.core import setup

setup(
    name='Bob-API',
    description='An assistant (like siri) that is used as a python API in projects.',
    version='development',
    url='https://github.com/Adrian-Gj/Bob-Assistant-API',
    author='Adrian Gjonca',
    author_email='AdrianGjonca100@gmail.com',
    packages=['bob',],
    license='GNU General Public License v3.0',
    install_requires=['lxml','wikipedia','send2trash',],
)
