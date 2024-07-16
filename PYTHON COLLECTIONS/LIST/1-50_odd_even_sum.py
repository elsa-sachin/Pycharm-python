lst=[]
even=[]
odd=[]

for i in range(1,51):
    lst.append(i)
print(lst)

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even list : {even}")
print(f"Odd list : {odd}")

print(sum(lst))
print(sum(even))
print(sum(odd))

