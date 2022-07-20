def main():

    A = [1, 2, 3,
    4, 5, 6,
    7, 8, 9]

    completion = 0
    turn = 'x'
    current_turn = 1

    while completion == 0:
        if turn == 'x':
            print("It is currently X's turn.\n")

            print(A[0], A[1], A[2])
            print(A[3], A[4], A[5])
            print(A[6], A[7], A[8])

            replace = input('\nEnter which number you would like to put your piece on:  ')

        if turn == 'o':
            print("It is currently O's turn.\n")

            print(A[0], A[1], A[2])
            print(A[3], A[4], A[5])
            print(A[6], A[7], A[8])

            replace = input('\nEnter which number you would like to put your piece on:  ')

        replace = int(replace)

        print('You have chosen {}.\n'.format(replace))

        A[replace-1] = turn

        if current_turn >= 3:

            if (A[0] == A[3] == A[6]) or (A[1] == A[4] == A[7]) or (A[2] == A[5] == A[8]) or (A[0] == A[1] == A[2]) or (A[3] == A[4] == A[5]) or (A[6] == A[7] == A[8]) or (A[0] == A[4] == A[8]) or (A[6] == A[4] == A[2]):

                print(A[0], A[1], A[2])
                print(A[3], A[4], A[5])
                print(A[6], A[7], A[8])

                print('\n{} wins!'.format(turn))

                completion = 1



        current_turn = current_turn + 1

        turn = turnswap(turn)


def turnswap(turn):

    if turn == 'x':
        newturn = 'o'
    else:
        newturn = 'x'

    return newturn


if __name__ == '__main__':
    main()