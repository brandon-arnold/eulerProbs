# copy-paste the input matrix into in.txt
M = [[int(n) for n in line.strip().split()] for line in open(".\in.txt", 'r')]
maxProduct = 0

def checkMax(product):
    global maxProduct
    if product > maxProduct:
        maxProduct = product

for i in range(0, len(M)):
    rowLen = len(M[i])
    is4FromTop = i > 3
    is4FromBottom = i < len(M) - 3
    for j in range(0, rowLen - 1):
        is4FromRight = rowLen - j > 3
        if is4FromRight:
            checkMax(M[i][j] * M[i][j + 1] * M[i][j + 2] * M[i][j + 3]) #horizontal
        if is4FromRight and is4FromBottom:
            checkMax(M[i][j] * M[i + 1][j] * M[i + 2][j] * M[i + 3][j]) #vertical
            checkMax(M[i][j] * M[i + 1][j + 1] * M[i + 2][j + 2] * M[i + 3][j + 3]) #down-right
        if is4FromRight and is4FromTop:
            checkMax(M[i][j] * M[i - 1][j + 1] * M[i - 2][j + 2] * M[i - 3][j + 3]) #up-right
    
print(maxProduct)
