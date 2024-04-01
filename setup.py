from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirement = []
    with open(file_path) as f:
        requirements = f.readline()

        requirement=[req.replace("\n", "") for req in requirements]
        return requirements
    
    if HYPEN_E_DOT in requirements:
        rerequirements.remove(HYPEN_E_DOT)



setup(
    name="Sensor_Fault_Detection",
    version="0.1.0",
    author="Jyoti",
    author_email="daradejyoti21@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt"),
)