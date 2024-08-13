dic={'Bike':500,'Bus':100,'car':890,'jeep':3000}

"""veh wt>2000 ,collect veh name"""

lst=[i for i in dic if dic[i]>2000]
print(lst)