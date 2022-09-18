def add(x,y):
    um=x+y
    return um
def sub(x,y):
    um=x-y
    return um
def mul(x,y):
    um=x*y
    return um
def div(x,y):
    um=x/y
    return um
print("\tCalculator")
print("\n1.Add\t2.sub\t3.Mul\t4.Div")
cmd=int(input("Enter your option ="))
a=int(input("Enter the value of a ="))
b=int(input("Enter the value of b ="))
if (cmd==1):
    print("The Added value is ",add(a,b))
elif(cmd==2):
    print("The Subracted value is ",sub(a,b))
elif(cmd==3):
    print("The Multiplied value is ",mul(a,b))
elif(cmd==4):
    print("The Divided value is ",div(a,b))
else:
    print("Invalid option")
