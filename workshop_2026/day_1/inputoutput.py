# input and output
# a=int(input("enter any number:"))
# print(a)
# swapping
# a = 10
# b = 20
# a, b = b, a
# print("a =", a)
# print("b =", b)
# sum of two numbers
# d=30
# e=20
# c=sum((d,e))
# print(c)
# #swapping
# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b
# print("a =", a)
# print("b =", b)
x = 100      # Global variable

def demo():
    y = 50   # Local variable
    print("Inside function:")
    print("Global x =", x)
    print("Local y =", y)

demo()

print("\nOutside function:")
print("Global x =", x)

# print(y)  # Error: y is not defined