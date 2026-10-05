numbers = [4, 7, 2, 7, 9, 7, 1]
target = 7
positions = []
for index in range(len(numbers)):
    if numbers[index] == target:
        positions.append(index)
first_position = -1
for index in range(len(numbers)):
    if numbers[index] == target:
        first_position = index
        break
print("Target number:", target)
print("Positions:", positions)
print("Number of Occurrences:", len(positions))

if first_position == -1:
    print("First occurrence: Not found")
else:
    print("First occurrence:", first_position)

