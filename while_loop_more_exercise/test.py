word = ""
c = False
n = False
o = False

while True:
    letter = input()
    if letter == "End":
        if c == True and n == True and o == True:
            print(word, end=" ")
        break

    if (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122):

        if letter == "c" and c == False:
            c = True
            if c == True and n == True and o == True:
                word += " "
                print(f"{word}", end="")
                word = ""
                c, n, o = False, False, False
                continue
            continue
        elif letter == "n" and n == False:
            n = True
            if c == True and n == True and o == True:
                word += " "
                print(f"{word}", end="")
                word = ""
                c, n, o = False, False, False
                continue
            continue
        elif letter == "o" and o == False:
            if c == True and n == True and o == True:
                word += " "
                print(f"{word}", end="")
                word = ""
                c, n, o = False, False, False
                continue
            o = True
            continue

        word += letter
    else:
        continue
