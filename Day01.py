with open ("input.txt") as f:
    file = f.readlines()

input = [int(line.removesuffix("\n")) for line in file]

increased = 0

for index in range(len(input)):
    if index == 0:
        continue
    if input[index] > input[index-1]:
        increased += 1

print(f"First solution: {increased}")


increased = 0

for i in range(len(input)):
    try:
        window_one = input[i] + input[i+1] + input[i+2]
        window_two = input[i+1] + input[i+2] + input[i+3]

        if window_two > window_one:
            increased += 1
    except:
        IndexError

print(f"Second solution: {increased}")
