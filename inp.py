# filename = inp  
# create rows and colums from file 
# take in input cols, rows
# output array with either true or false
 

def input(inp):
    try:
    cells = [] 


     # read in file 
    with open(inp) as f:
        cells = f.read()

    else:
        r = int(input('rows'))
        c = int(input('columns'))
    


