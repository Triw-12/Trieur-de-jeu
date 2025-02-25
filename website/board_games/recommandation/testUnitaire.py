
X0 = [1,0,0]
X1 = [0,1,0]
X2 = [2,0,0]
X3 = [1,1,1]

u0 = [4,0,0,0]
u1 = [0,0,0,0]
u2 = [0,4,4,4]
u3 = [0,8,0,8]

mu0 = 1
mu1 = 0
mu2 = 3
mu3 = 4

nb_jeux_joues = [u0,u1,u2,u3]

from collaboratif import *


##Test collaboratif

def testPearson() : 
	assert(pearson(nb_jeux_joues,0,1,mu0,mu1) == 0)
	assert(pearson(nb_jeux_joues,0,0,mu0,mu0) == 1)
	assert(pearson(nb_jeux_joues,0,2,mu0,mu2) == -1)

def testMoyennePonderee():
	assert(int(moyennePonderee(nb_jeux_joues,0,1)) == 0)
	assert(int(moyennePonderee(nb_jeux_joues,2,3)) == 4)
	assert(moyennePonderee(nb_jeux_joues,1,0) == 0)

def testCollaboratif():
	assert(collaboratif(nb_jeux_joues,0)[2] == 0)
	assert(collaboratif(nb_jeux_joues,1) == [0,0,0,0])
	assert(int(10*collaboratif(nb_jeux_joues,2)[1]) == 46)

testPearson()
testMoyennePonderee()
testCollaboratif()
