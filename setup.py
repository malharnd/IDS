from setuptools import find_packages,setup
from typing import List

dot_e = '-e .'

def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    if dot_e in requirements:
        requirements.remove(dot_e)
    return requirements
        

setup(
    name='IDS',
    version='0.0.1',
    author='Malhar',
    author_email='malhar.dhawle@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)