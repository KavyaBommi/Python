until=int(input())
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(2,until):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")
print()    