import string
import sys
# text = input()
text = "The​ ​ quick​ ​ brown​ ​ fox​ ​ jumps​ ​ over​ ​ the lazy​ ​ dog."
# text = "The​ ​ snow​ ​ glows​ ​ white​ ​ on​ ​ the​ ​ mountain tonight,​ ​ Not​ ​ a ​ ​ footprint​ ​ to​ ​ be​ ​ seen. A​ ​ kingdom​ ​ of​ ​ isolation,​ ​ and​ ​ it​ ​ looks like​ ​ I'm​ ​ the​ ​ Queen.​ ​ The ​wind​ ​ is howling​ ​ like​ ​ this​ ​ swirling​ ​ storm inside.​ ​ Couldn't​ ​ keep​ ​ it​ ​ in;​ ​ Heaven knows​ ​ I've​ ​ tried"


def New_text(text):
    new = ''
    for char in text:
        if char.isalpha() == True:
            new += char.lower()
    return new


new_text = New_text(text)
# print(new_text)

alphabet = string.ascii_lowercase
count = 0
for i in alphabet:
    if i not in new_text:
        print("Not pangram")
        sys.exit(0)
print(len(new_text), " char long pangram")
