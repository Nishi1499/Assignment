#Factorial of any number n is represented by n! and is equal to 1*2*3*.....*(n-1)*n.
num=int(input("Enter a number"))
i=1
sum=1
while(i<num):
    var = num * i
    sum=var*sum
    num=num-1
print("The Factorial:",sum)