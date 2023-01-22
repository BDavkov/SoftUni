username = input()
password = input()

while True:
    counter = input()
    if counter == password:
        print(f"Welcome {username}!")
        break
