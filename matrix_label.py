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
def create_matrix(r,c):
    matrix=[]
    for i in range(r):
        a=[]
        for j in range(c):
            k=''
            a.append(k)
        matrix.append(a)
    return(matrix)

def display_matrix(matrix):
    for i in range(len(matrix[0])):
        print('*---'*len(matrix[0]),end='')
        for j in range(len(matrix)):
            print('|',end='')
            print((matrix[i][j]),end='')
        print()
m=create_matrix(3,3)
# print(m)
display_matrix(m)

def label_matrix():




    