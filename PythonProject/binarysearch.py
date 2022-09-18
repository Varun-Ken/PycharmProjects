x=[]
n=int(input("Enter the length:"))
for i in range (1,int(n)+1):
    k=int(input("Enter value:"))
    x.append(k)
print(x)
s = int(input("Enter the element to be searched ="))
st = 0
sp = len(x) - 1
while st <= sp:
    mid = (st + sp) // 2
    if s == x[mid]:
        print("Element found at ", mid + 1)
        break
    elif s < x[mid]:
        sp = mid - 1
    else:
        st = mid + 1
else:
    print("Not found")