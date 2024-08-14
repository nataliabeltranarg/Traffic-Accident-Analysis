from setuptools import setup, find_packages

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='dataanalysis',
    version='0.2',
    packages=find_packages(),
    install_requires=get_requirements()
)
