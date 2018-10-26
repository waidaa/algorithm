def makesubfield(n):
    subfield = i2a.array.make2d(n//2,n)
    
    subfield[0][n//2-1] = 1
    
    for i in range(1,n//2):
        for j in range(n-1):
            if j == 0:
                subfield[i][j] = subfield[i-1][j+1]
            elif j == n-2:
                subfield[i][j] = subfield[i-1][j-1]
            else:
                subfield[i][j] = (subfield[i-1][j-1] + subfield[i-1][j+1])%2
    
    for i in range(n//2):
        for j in range(n):
            if subfield[i][n//2-1-j] == 1:
                pass
            else:
                subfield[i][n//2-1-j] = subfield[i][n//2-2-j]
    
    
    return subfield


    
subfield = makesubfield(1000)

field = i2a.array.make2d(1000,1000)

for i in range(1000//2):
    field[2*i] = subfield[i]
    field[2*i+1] = subfield[i]

newfield = i2a.array.make2d(1000,1000)
for i in range(1000):
    for j in range(1000):
        newfield[i][j] = 1 - field[i][j]

%matplotlib
i2a.plot.image_show(newfield)
