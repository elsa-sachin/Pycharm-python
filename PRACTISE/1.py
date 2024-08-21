w=input("Enter s string :")
for i in range(len(w)):
    flag=0
    if i==0:
        if ('a'<=w[i]<='z') or ('A'<=w[i]<='Z') or (w[i]=='_') :
            flag=1

        else:
            print("not valid")
            break
    elif ('0'<=w[i]<='9') or('a'<=w[i]<='z') or ('A'<=w[i]<='Z') or (w[i]=='_'):
            flag=1

    else:
        print("not valid ")
        break
if flag==1:
    print("valid")


