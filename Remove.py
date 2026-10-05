Marks = [50, -100, -90, 200, 70, 90, 89,80]
largest = Marks[0]
for mark in Marks:
    if mark > largest:
        largest = mark
print("The largest mark is:", largest)
