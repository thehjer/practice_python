f=open('table.csv')
fout=open('table_out.csv','w')
main_list=[]
for l in f:
    l=l.strip()
    l=l.split(';')
    main_list.append(l)
for l in main_list:
    s=''
    for i in l:
        s=s+i+','   
    fout.write(s+'\n')

    











    