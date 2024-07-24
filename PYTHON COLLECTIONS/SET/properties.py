"""DEFINITION"""
st={}
print(type(st))   #an empty set is a dictionary

st={1,2,3,4}    # this is a set

st=set()     # a function set() is used to define empty set


""" SUPPORTS HETEROGENOUS DATA"""
st={1,2,'python'}
print(st)

"""DOES NOT SUPPORT DUPLICATE VALUES"""
st={1,2,'python',2}
print(st)
st1={1,True,0,False}
print(st1)

"INSERTION ORDER IS not  PRESERVED"


"""MUTABLE"""

