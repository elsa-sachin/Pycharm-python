"""DEFNITION"""

dic={}
"""KEY   :VALUE     PAIR"""
""" id   :101 
    fname:Elsa  
    lname:Maria
    age  :27  
    prof :DS
    sal  :1200"""
dic={'id':101,'fname':'Elsa','lname':'Maria','age':20,'prof':'DS','sal':1200}
print(dic)

"""SUPPORTS HETEROGENEOUS DATA"""

"""INSERTION ORDER IS PRESERVED"""

"""DOES NOT SUPPORT DUPLICATE KEYS"""
dic1={'id':101,'fname':'Elsa','lname':'Maria','age':20,'age':21}
print(dic1)

"""SUPPORTS DUPLICATE VALUES"""
dic2={'id':101,'fname':'Elsa','lname':'Maria','age':20,'age1':20}
print(dic2)

"""MUTABLE"""
