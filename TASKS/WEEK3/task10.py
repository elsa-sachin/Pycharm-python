"""Write a python program to read four numbers (representing the four octets of an IP) and print the next five IP address
Eg:
Input:
192 168 255 252
----------Output---------
192 168 255 253
192 168 255 254
192 168 255 255
192 169 0 0
192 169 0 1
"""


first=int(input("Enter first octet: "))
sec=int(input("Enter second octet: "))
third=int(input("Enter third octet: "))
fourth=int(input("Enter fourth octet: "))

start=fourth+1
end=fourth+6

if(1<=first<=255)and (0<=sec<=255) and(0<=third<=255)and(0<=fourth<=255):
    for i in range(start,end):
        fourth=fourth+1
        if fourth>255:
            fourth=(fourth%255)-1
            third=third+1

            if third>255:
                third=(third%255)-1
                sec=sec+1

                if sec>255:
                    sec=(sec%255)-1
                    first=first+1

                    if first>255:
                        print("No more available IP")
                        break

        print(f"{first} {sec} {third} {fourth}")
else:
    print("invalid input")