f=open("C:\\Users\\Elsamaria Sachin\\OneDrive\\ドキュメント\\py ds\\movies_cleaned_pandas.csv",'r')

for i in f:
    data=i.rstrip('\n').split(',')
    print(data)
    rate=data[3]
    yr=data[2]
    