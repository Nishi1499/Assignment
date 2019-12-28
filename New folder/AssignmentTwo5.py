num =int(input("Enter a number that you want a table"))
abc=1
var=0
ss=0
for i in range(1,11):
    abc=num*i
    print(abc,"=",num,"*",i)
    var = abc + var
print("this is sum",var)






