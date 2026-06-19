# if(condn):
#     statements
# else:
#    statements
num=int(input("enter any number:"))
if(num%2==0):
    print("even")
else:
    print("odd")
 
# cases
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")