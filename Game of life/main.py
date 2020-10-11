import inp, nextgen, reproduce, time, sys, os

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter filename")
    arr, rows, cols = inp.input(filename)

    while True:
        for r in range(rows):
            for c in range(cols):
                if arr[r][c] == True:
                    print('*', end='')
                else:
                    print('.', end='')
            print('')
        print('')

        dead = []
        born = []
        for r in range(rows):
            for c in range(cols):
                if reproduce.reproduce(arr, r, c) != arr[r][c]:
                    born.append([r,c])
                if nextgen.nextgen(arr, r, c) != arr[r][c]:
                    dead.append([r,c])

        for r,c in born:
            arr[r][c] = True

        for r,c in dead:
            arr[r][c] = False

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
