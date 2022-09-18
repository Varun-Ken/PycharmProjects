x=[]
n=int(input("Enter the length:"))
for i in range (1,int(n)+1):
    k=int(input("Enter value:"))
    x.append(k)
print(x)
s=int(input("Enter the number to be seached ="))
for i in range(0,len(x),1):
    if(s==x[i]):
        print("Element found at ",i+1)
        break
else:
    print("Not found")