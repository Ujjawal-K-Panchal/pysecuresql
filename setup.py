# -*- coding: utf-8 -*-
"""
Title: pyauth setup.
    
Created on Tue Dec 9 15:27:19 2021
@author: Ujjawal.K.Panchal, @Email: ujjawalpanchal32@gmail.com
Copyright (C) Ujjawal K. Panchal - All Rights Reserved.
---
"""
from setuptools import setup

desc = """
        Title: pysecuresql: Simple SQL connection handling by avoiding SQL injection.
	---
	Contents:	
		1.) ssql.: Secure SQL.
        
  @author: Ujjawal.K.Panchal, @Email: ujjawalpanchal32@gmail.com
	---
        Copyright (C) Ujjawal K. Panchal - All Rights Reserved.	
	---
    """
package_list = ['ssql',]

setup(
    name = "pysecuresql",
    version = "1.0.0",
    description = desc,
    url = "#",
    author = "Ujjawal K. Panchal",
    author_email = "ujjawalpanchal32@gmail.com",
    license = "BSD3.",
    packages = package_list,
    install_requires=["mysql-connector>=2.2.9",],
    python_requires=">=3.8.5",
    zip_safe = False
)