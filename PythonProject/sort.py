n=[]    #l=list
x=int(input("Enter the length of the List :"))  #x=length of the list
for i in range(0,x):
    t=int(input("Enter the Element No.{} :".format(i + 1)))    #t=temporary variable
    n.append(t)
print("List =",n)
for f in range(len(n)-1,0,-1):
    maxpos=0
    for l in range(1,f+1):
        if n[l]>n[maxpos]:
               maxpos=l
    t=n[f]
    n[f]=n[maxpos]
    n[maxpos]=t
print("Sorted List =",n)

'''print("\n")
n = [54, 6, 3, 89, 21]
print(n)
def sort(n):
    for i in range(0, len(n), 1):
        t = 0
        for j in range(1, i):
            if n[j] > n[t]:
                t = j
        tp: int = n[i]
        n[i] = n[t]
        n[t] = tp
sort (n)
print(n)'''
