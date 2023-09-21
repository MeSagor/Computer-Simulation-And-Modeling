
def mid_square_method(seed):
    square = str(seed ** 2)
    while len(square) != 8:
        square = '0' + square
    next_seed = int(square[2:6])
    return next_seed, square


seed = 7182

print("................................")
print("|  i  |  Zi  |  Ui  |  Zi x Zi |")
print("................................")
i = 0
while True:
    next_seed, square = mid_square_method(seed)
    print(f'| {i:3} | {seed:4} | {next_seed:4} | {square:8} |')
    seed = next_seed
    i += 1
    if next_seed == 0:
        break

print("................................")
print(f'Total Random Numbers: {i}')