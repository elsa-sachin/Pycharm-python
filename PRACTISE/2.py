word='luminar _techno 908alab'
word+=' '
identifier=''
for i in word:
    if i !=' ':
        identifier+=i
    for j in range(len(identifier)):
        f=0
        if j==0:
            if ('a'<=identifier[j]<='z') or ('A'<=identifier[j]<='Z') or (identifier[j]=='_'):
                f=1
            else:
                print("Not valid")
        elif ('0'<=identifier[j]<='9')or('a'<=identifier[j]<='z') or ('A'<=identifier[j]<='Z') or (identifier[j]=='_'):
             f=1
        else:
            print("Invalid")
    if f==1:
        print("Valid")




