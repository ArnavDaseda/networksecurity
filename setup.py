from setuptools import find_packages,setup
from typing import List

def get_requriments()->List[str]:
    requriment_list:List[str]=[]
    try:
        with open ("requirments.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requriments = line.strip()
                if requriments and requriments!= "e.":
                     requriment_list.apend(requriments)

    except FileNotFoundError:
        print("requriments.txt does not exist")

    return requriment_list

setup(
    name="NetworkSecurity",
    version="0.1",
    author="Arnav",
    author_email="arnav@email.com",
    packages= find_packages(),
    install_requries=get_requriments()
)