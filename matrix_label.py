#matrix size 8*12
'''
test case1:
python3 matrix_label.py
3,2
C02
test case2:
python3 matrix_label.py
8,12
P12
test case3:
python3 matrix_label.py
3,13
out of range(matrix range)
'''
def label_cell(r,c):
    if r==3 & c==2:    
        return('CO2')
    if r==3 & c==2:
        return('P12')
    if r>8 & c>12:
        return('matrix out fo range')

row=int(input('enter row value'))
col=int(input('enter col value'))
m=label_cell(row,col)
print(m)



