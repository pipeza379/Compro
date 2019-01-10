def det(m):
  if len(m) == 2:
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]
  else:
    det=0
    for c in range(len(m)):
      det+=m[0][c]*cofactor(m,0,c)
    return det
    
def minor(m,i,j):
  return det([row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])])

def cofactor(m,i,j):
  return (-1)**(i+j)*minor(m,i,j)

def tran(m):
  new_m =[]
  for i in range(len(m)):
    row=[]
    for j in range(len(m[0])):
      row.append(m[j][i])
    new_m.append(row)
  return new_m

def adj(m):
  new_m=[]
  for i in range(len(m)):
    row=[]
    for j in range(len(m)):
      row.append(cofactor(m,i,j))
    new_m.append(row)
  return tran(new_m)
    
def inverse(m):
  try:
    new_m = adj(m)
    for i in range(len(new_m)):
      for j in range(len(new_m)):
        new_m[i][j] = new_m[i][j]/det(m)
    return new_m
  except:
    return 'invalid'

def matrix_mul(a,b):
  total =[]
  for i in range(len(a)):
    result=[]
    for j in range(len(b[i])):
      sum=0
      for k in range(len(a[i])):
        sum+=a[i][k]*b[k][j]
      result.append(sum)
    total.append(result)

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
n = [[1,3,-2,1],[5,1,0,-1],[0,1,0,-2],[2,-1,0,3]]
     
print(minor(m,1,1))
print(cofactor(m,1,1))
print(tran(m))
print(adj(n))
print(det(n))
print(inverse(n))
