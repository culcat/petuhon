
a=['1','2','5','4','1']
m = max(a)
i = -1
while i< len(a):
    i=i+1
    if a[i] == m:
        a[i]=a[i]*2
        print(a)


