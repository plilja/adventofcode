def step1(first_row):
    def is_safe(prev_row, i):
        left = prev_row[i - 1] if i > 0 else True
        right = prev_row[i + 1] if i < len(prev_row) - 1 else True
        return not (right ^ left)

    row = [True if x == '.' else False for x in first_row]
    ans = 0
    for i in range(0, 40):
        ans += len(list(filter(lambda x: x, row)))
        row = [True if is_safe(row, i) else False for i in range(0, len(row))]
    return ans


row = input()
print(step1(row))
