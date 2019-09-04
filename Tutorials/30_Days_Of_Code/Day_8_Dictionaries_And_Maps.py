n = int(input())
phone_book = {}

for i in range(0, n):
    name, number = input().split(" ")
    phone_book[name] = number

while(True):
    try:
        name = input()
    except EOFError:
        break

    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not found")