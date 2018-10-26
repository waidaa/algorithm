import numpy as np
import matplotlib.pyplot as plt

def makesubfield(n):
    subfield = np.zeros([n//2,n]  )
    
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

def makefield(n):
    field = np.zeros([n,n])
    subfield = makesubfield(n)
    
    for i in range(n//2):
        field[2*i] = subfield[i]
        field[2*i+1] = subfield[i]
    
    return field

def reverse(field):
    n = len(field)
    field = field * (-1) + np.ones([n,n])
    
    return field

def main(n):
    field = makefield(n)
    field = reverse(field)
    plt.imshow(field, cmap = 'gray', vmin = 0, vmax = 1, interpolation = 'none')
    plt.show()
    
