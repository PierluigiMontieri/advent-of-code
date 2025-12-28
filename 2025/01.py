input_folder = "input/"

with open(input_folder + "01.txt") as file:
    rotations = [int(line[1:]) * (1 if line[0] == 'R' else -1) for line in file]

# part 1
pointer = 50
password = 0
for rotation in rotations:
    pointer = (pointer + rotation) % 100
    if pointer == 0:
        password += 1
print(password)

# part 2
pointer = 50
password = 0
for rotation in rotations:
    if rotation > 0:
        password += (pointer + rotation) // 100
    else:
        password -= ((pointer + rotation) // 100)
        if (pointer + rotation) % 100 == 0:
            password += 1
        if pointer == 0:
            password -= 1

    pointer = (pointer + rotation) % 100
print(password)

    

