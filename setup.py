#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:11:31 2023

@author: macbook
"""

from setup_tools import find_packages,setup
from typing import List

HYPEHEN_E_DOT="-e."
def read_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requriment_list=file_obj.readlines()
        requriment_list=[eachline.replace("\n") for eachline in requriment_list]
        if HYPEHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPEHEN_E_DOT)
            
    return requriment_list


    


setup(
      name='FirstTestPacakge',
      version="0.0.1",
      author='AMD',
      pacakges=find_packages(),
      install_requrires=['pandas','numpy'])

#kiva install _requires la apan requirement.txt vachun info devu shakto
