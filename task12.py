from getpass import getpass

password = getpass("Password: ")
conform = getpass("Conform password: ")

if password == conform:
    print("Parol mos keldi")
else:
    print("Parol mos kelmadi")