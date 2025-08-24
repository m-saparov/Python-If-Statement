a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b and b == c:
    print("Teng tomonli")

if (a == b and b != c) or (a == c and a != b) or (b == c and b != a):
    print("Teng yonli")

if a != b and  a != c and b != c:
    print("Turli tomonli")