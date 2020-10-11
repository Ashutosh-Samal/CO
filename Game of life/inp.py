# create rows and colums from file
# take in input cols, rows
# output array with either true or false


def input(filename):
    cells = []
     # read in file
    with open(filename) as f:
        cells = f.readlines()
    rows, cols = [int(x) for x in cells[0].strip('\n').split(' ')]
    cells = [x.strip() for x in cells[1:]]
    arr = []
    for i in range(rows):
        temp=[]
        for j in range(cols):
            if cells[i][j] == '*':
                temp.append(True)
            else:
                temp.append(False)
        arr.append(temp)
    return arr, rows, cols
