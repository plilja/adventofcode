import sys


def bin_search(pattern, low_char, high_char, upper):
    low, high = 0, upper
    for i in range(0, len(pattern)):
        c = pattern[i]
        m = low + (high - low + 1) // 2
        if c == high_char:
            low = m
        else:
            assert c == low_char
            high = m - 1
    return low


def calc_seat_id(boarding_pass):
    row = bin_search(boarding_pass[0:7], 'F', 'B', 127)
    col = bin_search(boarding_pass[7:], 'L', 'R', 7)
    return 8 * row + col


def step1(boarding_passes):
    return max(map(calc_seat_id, boarding_passes))


def step2(boarding_passes):
    seat_ids = sorted(map(calc_seat_id, boarding_passes))
    prev_id = -1
    best_edge_dist = -float('inf')
    result = None
    for i, seat_id in enumerate(seat_ids):
        if seat_id - prev_id == 2:
            # this might be my seat, take the one furthest from the
            # edges since problem statement states that seat is
            # located in the middle and there are missing seats close
            # to edges
            dist = min(i, len(seat_ids) - i)
            if dist > best_edge_dist:
                best_edge_dist = dist
                result = seat_id - 1
        prev_id = seat_id
    return result


boarding_passes = [line.strip() for line in sys.stdin.readlines()]
print(step1(boarding_passes))
print(step2(boarding_passes))
