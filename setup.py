from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(filepath:str)->List[str]:     
    """
    This function will return the list of requirements
    NB: dont forget to add -e.
    """
    requirements=[]
    with open(filepath) as file_obj:
        requirements = file_obj.readline()
        [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    description='',
    author='Herb',
    packages=find_packages(),
    author_email='hcaxtonmartins@gmail.com',
    install_requires=get_requirements('requirements.txt')
)
