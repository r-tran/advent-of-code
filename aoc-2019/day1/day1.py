masses = map(int, open('data.txt', 'r').readlines())

# part 1
def calc_fuel(mass):
    return mass // 3 - 2

print(sum(calc_fuel(m) for m in masses))

# part 2
def calc_additional_fuel(mass):
    total, fuel = 0, calc_fuel(mass)
    while fuel > 0:
        total += fuel
        fuel = calc_fuel(fuel)
    return total

print(sum(calc_additional_fuel(m) for m in masses))

