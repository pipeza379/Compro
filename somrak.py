i = 1
count = 0
somrak = 0
find = False
while i <= 5:
    chk = False
    sum = ""
    st = input()
    st = st.lower()
    for a in st:
        sum += a
        if sum == "somrak":
            count += 1
            sum = ""
            chk = True
        i += 1
        if chk == True:
            somrak += 1
        else:
            somrak = 0
        if somrak >= 3:
            find = True
if find == True:
    print("Love Love Somsri")
else:
    print("Mai rak mai tong ma care")
print("\"somrak\" ::", count, "sentences")
