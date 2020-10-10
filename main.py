import inp, nextgen, reproduce, time, sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter filename")
    arr = inp.input(filename)
    while True:
        temp = arr
        for r in range(len(arr)):
            for c in range(len(arr[0])):
                temp[r][c] = reproduce.reproduce(arr, r, c)
                temp[r][c] = nextgen.nextgen(arr, r, c)
                if temp[r][c] == True:
                    print('*', end='')
                else:
                    print('.', end='')
            print('')
        print('')
        time.sleep(1)
