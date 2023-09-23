def step1(n):
    recipes = [3, 7]
    e1, e2 = 0, 1
    while len(recipes) < n + 10:
        r1 = recipes[e1]
        r2 = recipes[e2]
        r = r1 + r2
        if r >= 10:
            recipes.append(r // 10)
        recipes.append(r % 10)
        e1 = (e1 + r1 + 1) % len(recipes)
        e2 = (e2 + r2 + 1) % len(recipes)
    return ''.join(map(str, recipes[n:n+10]))


def step2(n):
    key = [int(i) for i in str(n)]
    recipes = [3, 7]
    e1, e2 = 0, 1
    while True:
        r1 = recipes[e1]
        r2 = recipes[e2]
        r = r1 + r2
        if r >= 10:
            recipes.append(r // 10)
            if recipes[-len(key):] == key:
                break
        recipes.append(r % 10)
        if recipes[-len(key):] == key:
            break
        e1 = (e1 + r1 + 1) % len(recipes)
        e2 = (e2 + r2 + 1) % len(recipes)
    return len(recipes) - len(key)


def main():
    n = int(input())
    print(step1(n))
    print(step2(n))  # This one is slow


if __name__ == '__main__':
    main()
