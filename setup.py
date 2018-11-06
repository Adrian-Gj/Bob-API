from distutils.core import setup

setup(
    name='Bob-API',
    version='dev',
    packages=['bob_api',],
    license='GNU General Public License v3.0',
    install_requires=['lxml','wikipedia','send2trash',],
)
