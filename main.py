import numpy as np
import matplotlib.pyplot as plt

def makepascal(n,d):
    pascal = np.zeros([n//2,n])

    pascal[0][n//2-1] = 1

    for i in range(1,n//2):
        for j in range(n-1):
            if j == 0:
                pascal[i][j] = pascal[i-1][j+1]
            elif j == n-2:
                pascal[i][j] = pascal[i-1][j-1]
            else:
                pascal[i][j] = (pascal[i-1][j-1] + pascal[i-1][j+1])%d

    return pascal

def makesubfield(n,d):
    subfield = makepascal(n,d)
    for i in range(n//2):
        for j in range(n):
            if subfield[i][n//2-1-j] >= 1:
                pass
            else:
                subfield[i][n//2-1-j] = subfield[i][n//2-2-j]


    return subfield


def makefield(n,d):
    field = np.zeros([n,n])
    subfield = makesubfield(n,d)

    for i in range(n//2):
        field[2*i] = subfield[i]
        field[2*i+1] = subfield[i]

    field = field/(d-1)

    return field


def reverse(field):
    n = len(field)
    field = field * (-1) + np.ones([n,n])

    return field


def main(n, d, bool):
    field = makefield(n,d)

    if bool == True:
        pass
    else:
        field = reverse(field)
    plt.imshow(field, cmap = 'gray', vmin = 0, vmax = 1, interpolation = 'none')
    plt.show()

main(5000,4,True)
