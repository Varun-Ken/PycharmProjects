from itertools import groupby
a=[{"name":"ss","age":55},{"name":"kk","age":45}]
gp=groupby(a,lambda x:x["name"])
for i,j in gp:
    print(i,list(j))
