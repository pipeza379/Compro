import random

def chAD(fail):
  if fail<=30:
    return False
  else:
    return True

def Aboss(T):
  if T<=20:
    return True
  else:
    return False
    
Hhp = 1500
Mhp = 2000
berserk = False
Hepo=2;bsp=1
while 1==1:

  atkH=random.randint(350,450)
  heal=random.randint(350,700)
  ran=random.randint(1,100)
  atkM=random.randint(250,350)
  
  print("Your hero has {} hp and the monster has {} hp".format(Hhp,Mhp))
  inp = input("(A)ttack/(D)efend/(U)se item : ")
  if inp=="A":
    if chAD(ran) == True:
      print("The moster loses {} hp".format(atkH*bsp))
      Mhp-=atkH*bsp
    else:
      print("Your Miss")

  if inp=="U":
    use=input("(H)ealing potion/(B)erserk potion : ")
    if use == "H":
      if Hepo>0:
        Hhp+=heal
        print("Hero's hp was restored by {} points".format(heal))
        Hepo-=1
        if Hepo==0:
          print("0 healing potion left")
        else:
          print("1 healing potion left")
      else:
        print("hero cannot heal (no healing potion left)")
    elif use == "B":
      if berserk==False:
        print("Berserk mode : on")
        berserk=True
  if berserk == True:
    bsp=2
    Hhp-=150
    print("The hero loses 150 hp from berserk mode")
    
  if inp=="D":
    if chAD(ran) == True:
      print("Defend success!!")
      continue
  
  if Aboss(ran) ==True:
    Hhp-=atkM
    print("The hero loses {} hp".format(atkM))
  else:
    print("Monster missed!")
  
  if Mhp<=0:
    if berserk == True and Hhp<=150:
      print("The hero loses 150 hp from berserk mode")
      print("Your hero has 0 hp and the monster has 0 hp")
      print("Draw")
      break
    print("The monster has 0 hp")
    print("You win")
    break
  elif Hhp<=0:
    print("Your hero has 0 hp")
    print("You lose")
    break
    
      