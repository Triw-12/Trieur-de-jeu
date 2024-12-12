from collaboratif import collaboratif
from contenus import contenus

def notes(M : list, n : int, m : int, MX : list, nx : int, u : int) :
	"""Hyppothèse : M est de dimension n*m, MX est de taille nx, u<m"""
	"""Renvois les notes hyppotétiques des jeux pour u conformément au donné de M et MX"""
	
	uMoy : int = sum(M[u]) / m
	uTot : int = sum(M[u])

	notesCollab = collaboratif(M,n,m,u,uTot)
	notesCont = contenus(M,n,m,MX,nx,uTot)

	notes[(notesCollab[i] + notesCont[i]) /2 for i in range (m)]
	
	return notes
