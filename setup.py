from xml.etree.ElementTree import VERSION
from setuptools import setup,find_packages
from typing import List




PROJECT_NAME = 'Housing-predictor'
VERSION = "0.0.2"
AUTHOR = "Satyajit"
DESCRIPION = "This is first fsds Nov batch Project"
PACKAGES = find_packages()
REQUIREMNT_FILE_NAME = 'requirments.txt'
HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    '''
    This function returns the list required to install in local machine which are included in requirments.txt

    '''
    with open(REQUIREMNT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    

setup(
    name = PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPION,
    packages=PACKAGES,
    install_requires = get_requirements_list()
)


if __name__ == "__main__":
    print(get_requirements_list())