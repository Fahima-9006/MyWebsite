Grade = int(input("Enter your grade: "))
if Grade >=97 and Grade <=100:
    print("A+")
elif Grade >=93 and Grade <=96:
    print("A")
elif Grade >=90 and Grade <=92:
    print("A-")
elif Grade >=87 and Grade <=89:
    print("B+")
elif Grade >=83 and Grade <=86:
    print("B")
elif Grade >=80 and Grade <=82:
    print("B-")
elif Grade >=77 and Grade <=79:
    print("C+")
elif Grade >=73 and Grade <=76:
    print("C")
elif Grade >=70 and Grade <=72:
    print("C-")
elif Grade >=67 and Grade <=69:
    print("D+")
elif Grade >=63 and Grade <=66:
    print("D")
elif Grade >=60 and Grade <=62:
    print("D-")
else:
    print("F")  

if Grade >=97 and Grade <= 100:
    print("You have an A+")
    if Grade >=93 and Grade <= 96:
        print("You have an A")
        if Grade >=90 and Grade <= 92:
            print("You have an A-")
            if Grade >=87 and Grade <=98:
                print ("You have a B+")
                if Grade >=83 and Grade <= 86:
                    print("You have a B")
                    if Grade >=80 and Grade <= 82:
                        print("You have a B-")
                        if Grade >= 77 and Grade <= 79:
                            print("You have a C+")
                            if Grade >=73 and Grade <=76:
                                print ("You have a C")
                                if Grade >=70 and Grade <= 72:
                                    print("You have a C-")
                                    if Grade >=67 and Grade <= 69:
                                        print("You have a D+")
                                        if Grade >=63 and Grade <= 66:
                                            print("You have a D")
                                            if Grade >=60 and Grade <= 62:
                                                print("You have a D-")
else:
    print("You have an F")  