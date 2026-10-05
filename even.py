n =100
for i in range(0, n, 1):
    if i % 2 == 0:
        for j in range(0, n, 1):
            if j % 2 != 0:
                print(i, "is even")
                print(j, "is odd")
                