from setuptools import find_packages, setup
setup(
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.5',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=['twine'],
    setup_requires=['pytest-runner', 'twine'],
    tests_require=['pytest==7.2.1'],
    test_suite='tests',
)