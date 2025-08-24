number = input("Phone number: ")

two = int(number[:2])

if two in (88, 90, 91, 93, 94, 95, 97, 99):
    if two == 90 or two == 91:
        print("Beeline")

    if two == 93 or two == 94:
        print("Ucell")

    if two == 95 or two == 97:
        print("Uzmobile")

    if two == 99 or two == 88:
        print("Mobiuz")
else:
    print("Nomalum operator")