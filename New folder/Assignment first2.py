#write a program to check a given input is integer or not
#var=input("Enter the number")
#if(var.isdigit()):
#    print("given number is integer")
#else:
 #   print("given number is another data type")

a=int(input("Enter a number"))
b=20
if type(a)==type(b):
    print("given number is integer")
else:
    print("given number is another data type")