numbers = [14, 8, 21, 21, 5, 17, 14]
Largest_distinct_value = []
Second_largest_value = []

for number in numbers:
    if number not in Largest_distinct_value:
        Largest_distinct_value.append(number)

Largest_distinct_value.sort(reverse=True)
if len(Largest_distinct_value) >= 2:
    Second_largest_value = Largest_distinct_value[1]
else:
    Second_largest_value = None

print("Largest distinct value:", Largest_distinct_value[0] if Largest_distinct_value else None)
print("Second largest value:", Second_largest_value)