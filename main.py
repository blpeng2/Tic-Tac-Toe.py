import numpy as np
import sys

arr = np.array(
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
    dtype= np.str_
)

def main():
    display_brd()
    x, y = map(int, input("Enter: ").split())
    while True:
        if x > 0 and x < 4 and y > 0 and y < 4:
            create_piece(player = 1, x = x, y = y)
            if check_fin() is True:
                break
        else:
            print("Input is wrong. Try Again Plz.")


def create_piece(player, x, y):
    if player is 1:
        arr[y - 1][x - 1] = 'O'
    else:
        arr[y - 1][x - 1] = 'X'

def display_brd():
    print("Tic-Tac-Toe: ")
    print("")
    print("--------------------------")
    print("")
    print(arr)
    print("")
    print("--------------------------")
    print("")

def check_fin():
    if arr[0][0] is 'O' and arr[0][1] is 'O' and arr[0][2] is 'O':
        ...
    if arr[0][0] is 'O' and arr[1][0] is 'O' and arr[2][0] is 'O':
        ...
    if arr[0][0] is 'O' and arr[1][1] is 'O' and arr[2][2] is 'O':
        ...

main()
print(arr)