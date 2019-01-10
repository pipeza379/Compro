#num = str(input())
# 0974
num = "0974"
lnum = list(num)
time = 0
while True:
    find = false = fail = 0
    guess = str(input("Guess : "))
    lg = list(guess)
    for i in range(0, 4):
        if lg[i] in lnum:
            if lg[i] == lnum[i]:
                find += 1
            else:
                false += 1
        else:
            fail += 1
    time += 1
    print("X"*find, end='')
    print("O"*false, end='')
    print("-"*fail, end='')
    print()
    if find == 4:
        print("You win the game after {} guess!!!".format(time))
        print("The number was {}".format(num))
        break
