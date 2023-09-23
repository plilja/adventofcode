def play(cups, iterations):
    successor = {}
    for i, c in enumerate(cups):
        successor[c] = cups[(i + 1) % len(cups)]

    highest = max(cups)
    current = cups[0]
    for i in range(0, iterations):
        picked_up = []
        next_to_pick_up = successor[current]
        for j in range(0, 3):
            picked_up.append(next_to_pick_up)
            next_to_pick_up = successor[next_to_pick_up]

        destination = current
        next_current = successor[picked_up[-1]]
        successor[current] = next_current
        current = next_current

        while True:
            destination -= 1
            if destination < 1:
                destination = highest
            if destination not in picked_up:
                break

        # Insert the picked up values
        successor[picked_up[-1]] = successor[destination]
        successor[destination] = picked_up[0]

    result = []
    node = 1
    visited = set()
    while node not in visited:
        result.append(node)
        visited.add(node)
        node = successor[node]
    return result[1:]


def step1(cups):
    return ''.join(map(str, play(cups, 100)))


def step2(cups):
    # This is slow, heavy looping isn't where Python shines
    m = max(cups) + 1
    for i in range(m, 1000001):
        cups.append(i)
    nums = play(cups, 10000000)
    return nums[0] * nums[1]


cups = [int(x) for x in input()]
print(step1(cups[::]))
print(step2(cups[::]))
