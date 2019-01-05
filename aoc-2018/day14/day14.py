def part1(n_recipes):
    a, b = 0, 1
    recipes = [3, 7]
    while len(recipes) < n_recipes + 10:
        score = str(recipes[a] + recipes[b])
        for digit in score:
            recipes.append(int(digit))

        a = (a + recipes[a] + 1) % len(recipes)
        b = (b + recipes[b] + 1) % len(recipes)
    
    return ''.join(list(map(str, recipes[n_recipes:n_recipes+10])))

def part2(sequence):
    a, b = 0, 1
    recipes = [3, 7]

    while True:
        score = str(recipes[a] + recipes[b])
        for digit in score:
            recipes.append(int(digit))
            if ''.join(list(map(str, recipes[len(recipes) - len(sequence):]))) == sequence:
                return len(recipes) - len(sequence)

        a = (a + recipes[a] + 1) % len(recipes)
        b = (b + recipes[b] + 1) % len(recipes)
    return -1

print(part2('51589'))
print(part2('01245'))
print(part2('92510'))
print(part2('59414'))
print(part2('077201'))
