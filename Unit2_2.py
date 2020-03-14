age = int(input("How old are you?"))
lean = input("Are you studing now?")
if 27 > age > 18 and lean == 'no':
    children = input("Do you have children?")
    if children == 'yes':
        number_children = int(input("How many children do you have?"))
        if number_children > 3:
            print("spare")
        elif number_children <= 3:
            height = int(input("How height are you?"))
            if height > 160:
                print("танкист")
            elif 160 >= height >= 150:
                print("подводная лодка")
            elif height <= 150:
                print("штаб")
    else:
        height = int(input("How height are you?"))
        if height > 160:
            print("танкист")
        elif 160 >= height >= 150:
            print("подводная лодка")
        elif height <= 150:
            print("штаб")
else:
    print("spare")
