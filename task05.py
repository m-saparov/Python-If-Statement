percent_5 = 100_000
percent_7 = 500_000

money = int(input("Omonat summasi: "))

if money < 500_000 and money > 0:
    if money < 100_000:
        print("5%")
    else:
        print("7%")
else:
    print("10%")