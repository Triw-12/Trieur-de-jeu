from contenus import *

X = [1,0,0,0,0]
Y = [2,0,0,0,0]
nX = 5

print(distance(X,Y))



M = [[2,1,4,0,0],[2,1,0,1,4],[0,2,2,3,1]]
X1 = [1,2,0]
X2 = [2,0,0]
X3 = [0,1,1]
X4 = [0,0,2]
X5 = [4,1,1]
MX = [X1,X2,X3,X4,X5]

print(barycentre(M,MX,1,sum(M[1])))

print(contenus(M,MX,1,sum(M[1])))


from collaboratif import *

print(collaboratif(M,1))


from hybride import *

notes(M,MX,1)
