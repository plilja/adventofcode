def solve(row, col):
    i = 1
    prev = 20151125
    while True:
        for j in range(0, i + 1):
            t = 252533 * prev % 33554393
            if i - j == col - 1 and j == row - 1:
                return t
            prev = t
        i += 1


def main():
    [row, col] = list(map(int, input().split()))
    print(solve(row, col))


if __name__ == '__main__':
    main()
