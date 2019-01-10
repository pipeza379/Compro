def makedic(word):
    word = ''.join(word.lower().split())
    wordlist = []
    for i in word:
        wordlist.append(i)
    dic = {}
    for i in wordlist:
        if i not in dic:
            dic.setdefault(str(i), 1)
        # else:
    return dic


def ch(check=True):
    if check == True:
        print("Perfect")
    else:
        print("Imperfect")
    exit()


word = input()
dic = makedic(word)
inv_dic = []
for i in dic:
    inv_dic.append(dic[i])
f = int(max(inv_dic, key=inv_dic.count))
count = check_count = 0
print(f)
print(dic)
# for j in dic:
# if f==dic[j]:
#  check_count+=1
# if check_count==1:
# ch(False)
for i in dic:
    # if dic[i]>1 and f-dic[i]==1:
        # ch(False)
    # if f-dic[i] != 0 and f-dic[i] != 1 and f-dic[i] !=-1:
        # ch(False)
    # if f-dic[i]==1 or f-dic[i]==-1:
        # count+=1
    # if count>1:
        # ch(False)
    # ch()
    if dic[i]-f == 0:
        continue
    elif dic[i]-1 == 0:
        count2 += 1
        continue
    elif dic[i]-f == -1 or dic[i]-f > 1:
        ch(False)
    else:
        count += 1
print(count)
if count < 2 and count2 < 2:
    ch()
ch(False)
