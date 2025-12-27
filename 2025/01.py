input_folder = "input/"
pointer = 50
password = 0

with open(input_folder + "01.txt") as file:
    rotations = [int(line[1:]) * (1 if line[0] == 'R' else -1) for line in file]

for rotation in rotations:
    pointer = (pointer + rotation) % 100
    if pointer == 0:
        password += 1

print(password)