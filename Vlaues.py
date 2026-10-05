values = [12, -5, 0, 7, -3, 0, 18, -1]
positive_values = []
negative_values = []
zero_values = []

for value in values:
    if value > 0:
        positive_values.append(value)
        print(f"{value} is postive.")
    elif value == 0:

        print(f"{ value} is Zero.")
    else:
        negative_values.append(value)
        print(f"{value} is Negative.")

    print(f"Positive values: {positive_values}")
    print(f"Negative values: {negative_values}")
    print(f"Zero values: {zero_values}")