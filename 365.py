way=input ()
i=int (input ())
j=int (input ())
x,y,t = 0,0,0
for a in range (0,len (way)):
    if way [a] =="U":
        y+=1
        t+=1
    elif way [a] =="D":
        y-=1
        t+=1
    elif way [a] =="R":
        x+=1
        t+=1
    elif way [a] =="L":
        x-=1
        t+=1
    if i==x and j==y:
        break

if i==x and j==y:
    print("Y")
    print (t)
else:
    print ("N")