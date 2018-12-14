def step1(n):
    recipes = [3, 7]
    elves = [0, 1]
    while len(recipes) < n + 10:
        recipes += [int(j) for j in str(sum(map(lambda i: recipes[i], elves)))]
        elves = [(1 + elve + recipes[elve]) % len(recipes) for elve in elves]
    return ''.join(map(str, recipes[n:n+10]))

n = int(input())
print(step1(n))
