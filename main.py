import numpy as np
import sys
input = sys.stdin.readline

def main():
    arr = np.array(
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        dtype= 'string'
    )

    print("Tic-Tac-Toe: ")
    print("")
    print("--------------------------")
    print("")
    print(arr)
    print("")
    print("--------------------------")
    print("")
    pos = input()
    print(pos)

main()