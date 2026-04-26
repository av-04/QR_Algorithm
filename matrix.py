from operator import add


def cr_matrix(size=21):
    return [[None for _ in range(size)] for _ in range(size)]


def add_finder(matrix, r, c):
    pattern = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    for i in range(7):
        for j in range(7):
            matrix[r + i][c + j] = pattern[i][j]


def add_patterns(matrix):
    add_finder(matrix, 0, 0)
    add_finder(matrix, 0, 14)
    add_finder(matrix, 14, 0)


# the actual logic of implementing the stream of bits into a qr format for even spread and error correction
def place_bits(matrix, bits):
    size = len(matrix)
    row = size - 1
    col = size - 1
    direction = -1
    idx = 0

    while col > 0:
        if col == 6:
            col -= 1

        for _ in range(size):
            for c in [col, col - 1]:
                if matrix[row][c] is None:
                    if idx < len(bits):
                        matrix[row][c] = int(bits[idx])
                        idx += 1
                    else:
                        matrix[row][c] = 0

            row += direction

            if row < 0 or row >= size:
                row -= direction
                direction *= -1
                break

        col -= 2


def print_mat(matrix):
    for row in matrix:
        print("".join("██" if x else "  " for x in row))
