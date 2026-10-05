number = [9, 100, -90, 50, 89, 70, 45, 80, 200]
for num in number:
    if num >100 or num <0:
        print("The number is invalid:", num)
    
    else: 
        if num >=90 and num <=100:
            print("The number is valid:", num, "and the grade is A")
        elif num >=80 and num <=89:
            print("The number is valid:", num, "and the grade is B")
        elif num >=70 and num <=79: 
            print("The number is valid:", num, "and the grade is C")
        elif num >=60 and num <=69:
            print("The number is valid:", num, "and the grade is D")
        elif num >=0 and num <=59:
            print("The number is valid:", num, "and the grade is F")
else:
    print("The number is valid:", num)                                   
