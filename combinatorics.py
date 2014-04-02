import math as m

try:
	from numpy import math as np_m
	numpy_math_loaded = True
except:
	numpy_math_loaded = False

try:
	from scipy import misc as sc_m
	scipy_misc_loaded = True
except:
	scipy_misc_loaded = False




def isInteger(num, tol = 10E-10):
	testVal = int(num)
	return abs(num-testVal)<=tol


def fact(nn,exact=True):
	'''
	Implements the factorial
	'''

	if scipy_misc_loaded:
		return sc_m.factorial(nn, exact=exact)

	elif numpy_math_loaded:
		return np_m.factorial(nn)

	else:
		return m.factorial(nn)

def perm(nn,kk,exact=True):
	'''
	Implements the permutations of picking kk
	distinguishable objects from a group of 
	nn distinguishable objects
	'''	
	if scipy_misc_loaded:
		return fact(kk)*comb(nn,kk,exact)

	else:
		return fact(nn) / fact(nn-kk)

def comb(nn,kk,exact=True):
	'''
	Implements the number of combinations of picking kk
	distinguishable objects from a group of 
	nn distinguishable objects
	'''	
	if scipy_misc_loaded:
		return sc_m.comb(nn,kk,exact = exact)
	
	else:
		# fact(nn) / fact(nn-kk)/fact(kk)
		return perm(nn,kk,exact)/fact(kk)

def multiCoef(nn,powerList):

	if sum(powerList) != nn :
		raise "Sum of the powers is not equal to n"

	value = fact(nn)

	for ii in powerList:

		value /= fact(ii)

	return value

def dist(nn,kk,exact=True):
	'''
	Implements the number of ways you can distribute
	kk indistinguishable objects into nn distinguishable
	containers.
	'''	
	return comb( nn+kk-1, kk, exact=exact)


def stirlinNum(nn,kk):
	'''
	Stirling Number of the second kind

	********************************************************************** 
	The following definition uses different notation than implemented code 
	**********************************************************************

	The number of ways to distribute m distinguishable objects among n distinguishable containers, 
	leaving not container empty is : 

	\sum\limit_{k=0}^{n} (-1)^k [n choose (n-k)] (n-k)^m

	(this is a surjection)

	We define the Stirling number of the second kind, S(m,n) 
	to be the number of ways to distribute m distinguishable objects among 
	n indistinguishable containers leaving no container empty.

	***** Can use this later *****
	Theorem :
		S( m + 1 , n ) = S(m , n - 1 ) + n * S(m,n)
	'''
	total = 0

	for ii in range(kk+1):
		term = (-1)**ii
		term*= comb(kk, ii)
		term*= (kk-ii)**nn

		total+= term

	return total // fact(kk)

def derange(nn):
	'''
	"A place for everything, and nothing in its place"

	A derangement of an ordered set (list) of n objects is 
	a permutation which returns none of them to its original place. 
	We denote the number of derangements of D_n.
	D_n ~= n! * exp(-1) for large values of n 
	'''
	nFact = fact(nn)

	kFact = 1

	total = nFact

	for kk in range(1,nn+1):
		kFact *= kk

		total += (-1)**kk * nFact / kFact

	return total

def numSurjective(nn,mm):
	'''
	The number of surjections from a set of size nn 
	a set of size mm
	f : NN ---> mm

	|NN| = nn
	|MM| = mm
	'''
	return fact(mm)*stirlinNum(nn,mm)