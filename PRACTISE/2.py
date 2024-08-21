word=' luminar _techno 908alab'
word+=' '
identifier=''
for i in word:
    if i !=' ':
        identifier+=i

    else:
        if identifier=='':     # this condition is given if there is a space at beginning
            continue
        print(identifier)
        for j in range(len(identifier)):
            f=0
            if j==0:
                if ('a'<=identifier[j]<='z') or ('A'<=identifier[j]<='Z') or (identifier[j]=='_'):
                    f=1

                else:
                    break
            elif ('0'<=identifier[j]<='9')or('a'<=identifier[j]<='z') or ('A'<=identifier[j]<='Z') or (identifier[j]=='_'):
                f=1
            else:
                break
        if f == 1:
            print(f"{identifier} :Valid")
        else:
            print(f"{identifier} :Invalid")


        identifier=" "
        print(identifier)





























