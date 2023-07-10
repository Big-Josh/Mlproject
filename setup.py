from setuptools import find_packages, setup

from typing import List

HYPHEN_DOT_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        
        # if HYPHEN_DOT_E in requirements:
        #     requirements.remove(HYPHEN_DOT_E)

        del requirements[-1]

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = "Big Josh",
    author_email = 'otoojoshua616@gmail.com',
    packages= find_packages(),
    install_require = get_requirements('requirements.txt')
)