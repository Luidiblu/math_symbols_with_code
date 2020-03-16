y = [[2,1],[4,3]]
z = [[1,2],[3,4]]
x = [[0,0],[0,0]]
for i in range(len(y)):
    for j in range(len(y[0])):
        x[i][j] = y[i][j] * z[i][j]
print(x)
# print(x) -> [[2, 2], [12, 12]]  