# create rows and colums from file
# take in input cols, rows
# output array with either true or false
<<<<<<< HEAD
=======
 

def input(inp):
    try:
    cells = [] 


     # read in file 
    with open(inp) as f:
        cells = f.read()

    else:
        r = int(input('rows'))
        c = int(input('columns'))
    

>>>>>>> 7a97fdd584d04aa46901a5b33778473e529c3283

def input(filename):
    cells = []
     # read in file
    with open(filename) as f:
        cells = f.readlines()
    rows, columns = [int(x) for x in cells[0].strip('\n').split(' ')]
    cells = [x.strip() for x in cells[1:]]
    arr = []
    for i in range(rows):
        temp=[]
        for j in range(columns):
            if cells[i][j] == '*':
                temp.append(True)
            else:
                temp.append(False)
        arr.append(temp)
    return arr
