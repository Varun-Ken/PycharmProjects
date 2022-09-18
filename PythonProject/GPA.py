def cegpa(x):
    credit=3
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
def magpa(x):
    credit=4
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
def dpsdgpa(x):
    credit=4
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
def dsgpa(x):
    credit=3
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
def oopsgpa(x):
    credit=3
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
def dslgpa(x):
    credit=2
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
def oopslgpa(x):
    credit=2
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
def dspdlgpa(x):
    credit=2
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
def islgpa(x):
    credit=1
    if x==1:
        y=((credit*10)/credit)
    elif x==2:
        y = ((credit * 9) / credit)
    elif x==3:
        y = ((credit * 8) / credit)
    elif x==4:
        y = ((credit * 7) / credit)
    elif x==5:
        y = ((credit * 6) / credit)
    return y
print("\t GPA CALCULATOR")
print("Enter the given options for the Grades:")
print("\t1.O \t2.A+\t3.A \t4.B+ \t5.B \t6.U")
ma=int(input("Enter the Grade for M-3:"))
mag=magpa(ma)
dpsd=int(input("Enter the Grade for DPSD :"))
dpsdg=dpsdgpa(dpsd)
ds=int(input("Enter the Grade for DS :"))
dsg=dsgpa(ds)
oops=int(input("Enter the Grade for OOPS :"))
oopsg=oopsgpa(oops)
ce=int(input("Enter the Grade for CE:"))
ceg=cegpa(ce)
dsl=int(input("Enter the Grade for DS Lab :"))
dslg=dslgpa(dsl)
oopsl=int(input("Enter the Grade for OOPS Lab :"))
oopslg=oopsgpa(oopsl)
dpsdl=int(input("Enter the Grade for DPSD Lab :"))
dpsdl=dspdlgpa(dpsdl)
isl=int(input("Enter the Grade for ISL Lab :"))
islg=islgpa(isl)
gpa=((mag+dsg+dpsdg+oopsg+ceg+oopslg+dslg+dpsdl+islg)/9)
print("GPA =%.3f"%gpa)