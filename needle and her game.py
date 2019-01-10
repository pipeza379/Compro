name = input("name : ")
word = input("word : ")
# word = "banana"


def Aeiou(char):
    pool = ["a", "e", "i", "o", "u"]
    if char[0] not in pool:
        return "needle"
    return "you"


def Check_char(word):
    new_word = ""
    for char in word:
        if char.isalpha() == True:
            new_word += char.lower()
    return new_word


def Build_word(word):
    you_p = 0
    needle_p = 0
    count = 0
    word = Check_char(word)
    for i in range(1, len(word)+1):
        for j in range(0, len(word)):
            check = Aeiou(word[j:j+i])
            if len(word[j:j+i]) == i:
                # count+=1
                if check == "needle":
                    needle_p += 1
                    # print(needle_p,end=". needle : ")
                elif check == "you":
                    you_p += 1
                    # print(you_p,end=". you : ")
                # print(word[j:j+i])
    # print("needle : ",needle_p)
    # print("you : ",you_p)
    return needle_p, you_p


needle, you = Build_word(word)
if needle < you:
    print(name, " ", you)
elif needle > you:
    print("Needle ", needle)
else:
    print("Draw")
