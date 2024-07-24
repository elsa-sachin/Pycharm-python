# if __name__ == '__main__':
#     N = int(input())
#
#     lst=[]
#     for i in range(N):
#         cond = input()
#         if "insert" in cond:
#             cond,i,e =cond.split()
#             lst.insert(int(i),int(e))
#         elif "print" in cond:
#             print(lst)
#         elif "remove" in cond:
#             cond,e=cond.split()
#             lst.remove(int(e))
#         elif "append" in cond:
#             cond,e=cond.split()
#             lst.append(int(e))
#         elif "sort" in cond:
#             lst.sort()
#         elif  "pop" in cond:
#             lst.pop()
#         else:
#             lst.reverse()


# if __name__ == '__main__':
#     students = []
#     grade = []
#     dup = []
#
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#         grade.append(score)
#     students.sort()
#     grade.sort()
#     for i in grade:
#         if i not in dup:
#             dup.append(i)
#     g = dup[1]
#     for n, s in students:
#         if s == g:
#             print(n)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     print(scores)
#     print(student_marks[query_name])
#     avg_marks = sum(student_marks[query_name]) / len(student_marks[query_name])


# def swap_case(s):
#     result=""
#     for char in s:
#         if char.islower():
#             result+=s.
#         elif s.isupper():
#             result+=s.lower()
#         else:
#             result+=char
#     return result

#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)



# Enter your code here. Read input from STDIN. Print output to STDOUT
# n=int(input())
#
# lst=tuple(map(int, input().split()))
#
# print(hash(lst))


# lst=[1,2,3,4,5,6]
# del lst[1:5]
# print(lst)

#
s='hello world'
str=s.split(" ")
for i in str:
    new=i.capitalize()
    new="".join(new)
    print(new)






