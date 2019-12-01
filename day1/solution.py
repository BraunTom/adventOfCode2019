import math

def with_file_open(path, fun):
    file = open(path, 'r')
    fun(file)
    file.close()

def calc_fuel(mass):
    return math.floor(int(mass) / 3) - 2

def calc_total_need(mass):
    sum = 0
    while calc_fuel(mass) > 0:
        sum += calc_fuel(mass)
        mass = calc_fuel(mass)
    return sum



with_file_open("input.txt", lambda file: print(sum(map(calc_total_need, file.readlines()))))
