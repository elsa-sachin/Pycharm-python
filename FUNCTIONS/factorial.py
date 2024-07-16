#
# """1ST METHOD"""
# def fact():
#     num=int(input("Enter the number :"))
#     factorial=1
#
#     for i in range(1,num+1):
#         factorial*=i
#     print(factorial)
#
# fact()

"""----------------------------------------------------------------------------------"""

"""2ND METHOD"""

# def fact(num):
#     factorial=1
#
#     for i in range(1,num+1):
#         factorial*=i
#     print(factorial)
#
#
#
# fact(3)

"""----------------------------------------------------------------------------------"""
"""3rd method"""

def fact(num):
    factorial=1

    for i in range(1,num+1):
        factorial*=i
    return factorial


print(fact(3))