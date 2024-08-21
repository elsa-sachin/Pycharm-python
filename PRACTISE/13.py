
# numbers = [3,5,45,97,32,22,10,19,39,43]
# lst=[i for i in numbers if i%2!=0 ]
# print(lst)


# lst=[i for i in range(1,1001) if i%7==0]
# print(lst)

# lst=[i for i in range(1,1001) if '3' in str(i)]
# print(lst)

# str="luminar techno lab kochi"
# lst=[i for i in str if i == " "]
# print(len(lst))

# sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# vow='aeiouAEIOU'
# lst=[i for i in sentence if i not in vow]
# print(len(lst))

# items = ["hi", 4, 8.99, 'apple', ('t,b','n')]
# lst=[(tuple([i,items[i]]))for i in range(len(items)) ]
# print(lst)

# lst_a=[1,2,3,4]
# lst_b=[2,3,4,5]
#
# lst=[i for i in lst_a if i in lst_b]
# print(lst)

# sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# words=sentence.split()
# lst=[i for i in words if i.isdigit()]
# print(lst)

# str="my name is elsamaria"
# words=str.split()
# lst=[i for i in words if len(i)<=4]
# print(lst)


# lst=["hello", "luminar","python","bigdata"]
# l=[i for i in lst.split(',')]
# print(l)

# sentence='This is a sample semtece'
# lst=[len(i) for i in sentence.split() ]
# print(lst)

# lst=["apple","banana","cherry"]
# lst1=[i[::-1] for i in lst]
# print(lst1)

# lst_a=[1,2,3,4,5,6,7,8,9]
# lst_b=[2,7,1,12]
# lst=[tuple([i,i]) for i in lst_a if i in lst_b]
# print(lst)

# lst=['apple','banana','cherry']
# lst1=[i[0] for i in lst]
# print(lst1)

# lst=[i**2 if i%2==0 else i**3 for i in range(-5,6)]
# print(lst)

# sen="This is a sample sentence"
# lst=[i.upper() for i in sen.split()]
# print(lst)

# lst=['apple','banana','cherry']
# v='aeiou'
# lst1=[('').join([j for j in i if j not in v])for i in lst]
# print(lst1)

# numbers = [-2, 3, -5, 7, -11]
# lst=[-i for i in numbers]
# print(lst)

# sentence='This is a sample semtece'
# lst=[(i,len(i)) for i in sentence.split() ]
# print(lst)

# lst=[(i,j) for i in range(1,11) for j in range(1,11) if (i+j)%2==0]
# print(lst)

# lst=['apple','banana','cherry']
# lst1=[i.capitalize() for i in lst]
# print(lst1)

# sen="Hello, World!"
# lst=[i for i in sen if not i.isalnum()]
# print(lst)

# lst=['apple','banana','cherry']
# v='aeiou'
# lst1=[''.join (["*" if j in v else j for j in i]) for i in lst]
# print(lst1)


# lst=['apple','banana','cherry']
# lst=[('').join (sorted(i))for i in lst]
# print(lst)