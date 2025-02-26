
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
vecteur_jeux = [X0,X1,X2,X3]

##Test collaboratif
from collaboratif import *

def testPearson() :
	"""pearson(nb_jeux_joues: list, joueur1: int, joueur2: int, joueur1_moyenne : float, joueur2_moyenne : float)"""
	assert(pearson(nb_jeux_joues,0,1,mu0,mu1) == 0)
	assert(pearson(nb_jeux_joues,0,0,mu0,mu0) == 1)
	assert(pearson(nb_jeux_joues,0,2,mu0,mu2) == -1)

def testMoyennePonderee():
	"""moyennePonderee(nb_jeux_joues: list, joueur: int, jeu: int)"""
	assert(int(moyennePonderee(nb_jeux_joues,0,1)) == 0)
	assert(int(moyennePonderee(nb_jeux_joues,2,3)) == 4)
	assert(moyennePonderee(nb_jeux_joues,1,0) == 0)

def testCollaboratif():
	"""collaboratif(nb_jeux_joues : list, joueur : int)"""
	assert(collaboratif(nb_jeux_joues,0)[2] == 0)
	assert(collaboratif(nb_jeux_joues,1) == [0,0,0,0])
	assert(int(10*collaboratif(nb_jeux_joues,2)[1]) == 46)
vecteur_jeux
testPearson()
testMoyennePonderee()
testCollaboratif()


##Test contenus
from contenus import *

def testDistance() :
	"""distance(v1: list, v2: list)"""
	assert(distance(X0,X2) )
	assert(distance(X2,X0) == 1)
	assert(distance(u0,u1) == 4)
	assert(distance(u1,u0) == 4)
	assert(distance(u2,u2) == 0)
	
def testDistancePond() :
	"""distancePond(v1: list, v2: list)"""
	assert(distancePond(X0,X0) == 0)
	assert(distancePond(X0,X2) == distancePond(X2,X0))
	assert(distancePond(X0,X1) == 4)

def testBarycentre() :
	"""barycentre(nb_jeux_joues: list, vecteur_jeux : list, joueur: int, nb_total_jouer : int)"""
	assert(barycentre(nb_jeux_joues,vecteur_jeux,1,0) == [0,0,0])
	assert(barycentre(nb_jeux_joues,vecteur_jeux,0,4) == [1,0,0])

def testValeurHypp():
	"""valeurHypp( dist : float, distmax : float, distmin : float, plus_jouer : int)"""
	assert(valeurHypp(20,30,10,30) == 15)
	assert(valeurHypp(1,1,1,1) == 1)

def testContenus():
	"""contenus(nb_jeux_joues :list , vecteur_jeux : list, joueur : int, nb_jeux_jouee_par_joueur : int)"""
	assert(contenus(nb_jeux_joues,vecteur_jeux,1,0) == [0,0,0,0])
	assert(int(contenus(nb_jeux_joues,vecteur_jeux,3,16)[0]) == 4)

testDistance()
testDistancePond()
testBarycentre()
testValeurHypp()
testContenus()
