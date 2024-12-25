input = "0 5601550 3914 852 50706 68 6 645371"
# input = "125 17"

rocks = list(map(str, input.split()))

for i in range(25):
    new_rocks = []
    for rock in rocks:
        if rock == '0':
            new_rocks.append('1')
        elif len(rock) % 2 == 0:
            left_rock = str(int(rock[:len(rock)//2]))
            right_rock = str(int(rock[len(rock)//2:]))
            new_rocks.append(left_rock)
            new_rocks.append(right_rock)
        else:
            new_rocks.append(str(int(rock) * 2024))
    rocks = new_rocks
print(len(rocks))