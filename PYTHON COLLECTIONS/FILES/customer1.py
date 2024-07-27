
f=open("C:\\Users\\Elsamaria Sachin\\OneDrive\\ドキュメント\\py ds\\customer1.txt",'r')
dic1= {}
dic2 = {}
for i in f:
    data=i.rstrip('\n').split(',')

    age=data[3]
    loc=data[-1]
    prof=data[4]


    """1. Age above 50 fname,lname,age,prof"""
    # if age>'50' :
    #     print(data[1:5])



    """2.Age range 25-40 fname,age.loc"""
    # if '25'<age<'40':
    #     print(data[1::2])


    """3.India work fname.lname.age,prof"""
    # if loc=='india':
    #     print(data[1:5])

    """4.India work and age >50 fname,lanme,age """
    # if loc=='india' and age>'50':
    #     print(data[1:4])


    """5.Uk work full data"""
    # if loc=='uk':
    #     print(data[0:])

    """6.IndiA work and prof dr fbame,lname,age,prof"""
    # if loc=="india" and prof=="Doctor":
    #     print(data[1:5])


    """7.Pilot fname,lname,age"""
    # if prof=='Pilot':
    #     print(data[1:4])


    """8.Each profession count"""
#     if prof not in dic1:
#         dic1[prof]=1
#     else:
#         dic1[prof]+=1
# print(dic1)



    """9.Each location count"""
#     if loc not in dic2:
#         dic2[loc] = 1
#     else:
#         dic2[loc] += 1
# print(dic2)
