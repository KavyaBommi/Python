#square pattern
n=int(input("enter number of rows"))
for i in range(1,n+1):
     for j in range(1,n+1):
        print("*",end=" ")
     print()
#inotqualsj square pattern
n=int(input("enter number of rows"))
for i in range(1,n+1):
     for j in range(1,n+1):
         if i==j:
             print(" ",end=" ")
         else:  
             print("*",end=" ")
     print()  
#print uppertriangular matrix
#print lower triangular matrix
#print rhombus
#print parallellogram
#print number pyramid