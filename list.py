list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
#print(list)
list = list.pop()
print(f"{list} has been removed from the list.")
friut = input("Enter a fruit name: ")
fruit = friut.lower()

if fruit in list:
    print(f"{fruit} is in the list.")
else:
    print(f"{friut} is not in the list.")
    new_friut = list.append(friut)
    print (f"{friut} has been added to the list.", new_friut)
