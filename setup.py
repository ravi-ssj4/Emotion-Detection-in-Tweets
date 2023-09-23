from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
        gives the list of required packages
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="Emotion detection in twitter tweets",
    version="0.0.1",
    author="Ravi Ranjan",
    author_email="raviranjan.ssj4@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)