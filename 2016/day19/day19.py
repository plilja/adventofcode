def step1(n):
    def iter(elves):
        if len(elves) == 1:
            [nr, _] = elves[0]
            return nr
        else:
            for i in range(0, len(elves)):
                [nr, num_presents] = elves[i]
                if num_presents != 0:
                    [next_nr, next_num_presents] = elves[(i + 1) % len(elves)]
                    elves[i] = [nr, num_presents + next_num_presents]
                    elves[(i + 1) % len(elves)] = [next_nr, 0]
            return iter(list(filter(lambda x: x[1] > 0, elves)))

    return iter([[i, 1] for i in range(1, n + 1)])


n = int(input())
print(step1(n))
