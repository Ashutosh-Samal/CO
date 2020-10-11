def nextgen(arr, i, j):
    if arr[i][j] == False:
        return False
    r = len(arr)
    c = len(arr[0])
    count = 0
    neighbours = []
    for a in range(i-1,i+2):
        for b in range(j-1,j+2):
            if a != i or b != j:
                if a >= 0 and a < r and b >= 0 and b < c:
                    neighbours.append([a,b])

    for indices in neighbours:
        x, y = indices
        if arr[x][y] == True:
            count+=1

    if count in range(2,4):
        return True
    return False
