from setuptools import find_packages, setup
setup(
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.11',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner', 'pytest-pylint'],
    tests_require=['pytest', 'pylint'],
    test_suite='tests',
)