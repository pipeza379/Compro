def makedic(word):
    word = ''.join(word.lower().split())
    wordlist = []
    for i in word:
        wordlist.append(i)
    dic = {}
    for i in wordlist:
        if i not in dic:
            dic.setdefault(str(i), 1)
        else:
            dic[i] += 1
    return dic


word = input()
word2 = input()
dic1 = makedic(word)
dic2 = makedic(word2)
print(dic1)
print(dic2)
if len(dic1) == len(dic2):
    for i in dic1:
        for j in dic2:
            if i == j:
                if dic1[i] != dic2[j]:
                    print("False")
                    exit()
    print('True')
else:
    print("False")
