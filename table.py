f=open('table.csv')
list=[]
for l in f:
    l=l.strip()
    l=l.split(',')
    list.append(l)
for i in list:
    print(i)










    