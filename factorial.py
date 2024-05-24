num=int(input("Enter a number:"))
n=num
fact=1
#i=1
while n>1:
    fact*=n
    n-=1
print("factorial of",num,"is:",fact)