def transposeMatrix(m):
    trans = [[ 0 for i in range(r)] for j in range(c)]
    for i in range(r):
        for j in range(c):
            trans[j][i]=mat[i][j]
    return trans

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

r=int(input("rows:"))
c=int(input("columns:"))
mat = [[int(input()) for x in range (c)] for y in range(r)]
inv=getMatrixInverse(mat)
trans=transposeMatrix(mat)
for o in mat:
    print(o)
print()
for r in trans:
    print(r)
print()
print(getMatrixDeternminant(mat))
print()
for i in inv:
    print(i)