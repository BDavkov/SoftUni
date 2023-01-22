word = ""
c = False
n = False
o = False
text = ""

while True:
    letter = input()
    if letter == "End":
        if c == True and n == True and o == True:
            print(word, end=" ")
        break
    elif (ord(letter) < 65) or (90 < ord(letter) < 97) or (ord(letter) > 122):
        continue

    if letter == "c":
        if not c:
            c = True
            continue
    elif letter == "n":
        if not n:
            n = True
            continue
    elif letter == "o":
        if not o:
            o = True
            continue

    if c == True and n == True and o == True:
        word += " "
        print(f"{word}", end="")
        word = ""
        c, n, o = False, False, False

    word += letter
