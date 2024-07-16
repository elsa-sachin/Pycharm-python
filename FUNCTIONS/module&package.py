"""python files is taken as modules"""

"""packages are collection of modules"""

"""" PACKAGE--PYTHON DIRECTORY 
      MODULE --PYTHON FILE
      """
# import packagename.modulename
# var=packagename.modulename.functioncall()


import FUNCTIONS.calculator
data=FUNCTIONS.calculator.add(2,3)
print(data)

data1=FUNCTIONS.calculator.sub(2,3)
print(data1)

#DRAWBACK:the package and module should be called each and every time for every function.
"""RECTIFICATION OF THE DRAWBACK"""

from FUNCTIONS.calculator import *  """* means importing all the functions from the calculator"""
print(add(20,30))
print(sub(20,30))


from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
       