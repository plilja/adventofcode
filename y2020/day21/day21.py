import sys
import re
import copy


def solve_helper(foods, remaining_ingredients, remaining_allergens, ingredient_to_allergen):
    if len(remaining_allergens) > len(remaining_ingredients):
        return []
    if not remaining_allergens:
        return [copy.deepcopy(ingredient_to_allergen)]
    allergen = remaining_allergens.pop()
    possible_ingredients = copy.deepcopy(remaining_ingredients)
    for ingredients, allergens in foods:
        if allergen in allergens:
            possible_ingredients &= ingredients
    result = []
    for ingredient in possible_ingredients:
        ingredient_to_allergen[ingredient] = allergen
        result += solve_helper(foods, remaining_ingredients - {ingredient}, remaining_allergens, ingredient_to_allergen)
        del ingredient_to_allergen[ingredient]
    remaining_allergens.append(allergen)
    return result


def solve(foods):
    all_ingredients = set()
    all_allergens = set()
    for ingredients, allergens in foods:
        all_ingredients |= ingredients
        all_allergens |= allergens
    solutions = solve_helper(foods, all_ingredients, list(all_allergens), {})
    assert len(solutions) == 1
    return solutions[0]


def step1(foods):
    solution = solve(foods)
    result = 0
    for ingredients, allergens in foods:
        for ingredient in ingredients:
            if ingredient not in solution:
                result += 1
    return result


def step2(foods):
    solution = solve(foods)
    d = {v: k for k, v in solution.items()}
    return ','.join([d[k] for k in sorted(d.keys())])


def read_input():
    result = []
    for line in sys.stdin:
        ingredients, allergens = re.match(r'([a-z ]+) \(contains ([a-z ,]+)\)', line).groups()
        result.append((set(ingredients.split(' ')), set(allergens.split(', '))))
    return result


def main():
    foods = read_input()
    print(step1(foods))
    print(step2(foods))


if __name__ == '__main__':
    main()
