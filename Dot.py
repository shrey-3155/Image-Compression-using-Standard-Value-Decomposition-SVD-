r1=int(input("rows1:"))
c1=int(input("columns1:"))

r2=int(input("rows2:"))
c2=int(input("columns2:"))

if(c1!=r2):
    print("Dimensions are incorrect")
else:
    mat1 = [[int(input()) for x in range(c1)] for y in range(r1)]
    mat2 = [[int(input()) for x in range(c2)] for y in range(r2)]
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                mul[i][j] += mat1[i][k] * mat2[k][j]
mul = [[0 for i in range(c2)] for j in range(r1)]

for o in mul:
    print(o)

