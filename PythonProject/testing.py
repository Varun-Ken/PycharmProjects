len=int(input("Enter the Length of the Array:"))
arr=[]
for i in range(0,len):
    l = int(input("Enter the {} Element:".format(i + 1)))
    arr.append(l)
print(arr)