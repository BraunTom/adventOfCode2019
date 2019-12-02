file = open('input.txt', 'r')
input = list(map(int, file.readline().split(',')))

def add(input, position):
    input[input[position + 3]] = input[input[position + 1]] + input[input[position + 2]]

def mul(input, position):
    input[input[position + 3]] = input[input[position + 1]] * input[input[position + 2]]


instruction_type = {1: add, 2: mul}

def eval_instructions(input):
    position = 0
    while input[position] != 99:
        instruction_type[input[position]](input, position)
        position += 4

eval_instructions(input)
print(input)

# 100 * 23 + 47

