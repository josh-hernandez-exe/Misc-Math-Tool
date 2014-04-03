'''
http://www.naturalnumbers.org/composites.html

http://primes.utm.edu/lists/small/millions/

The first million primes
first : 2
last  :15,485,863

This module is still in development.
I am still deciding if this is still the best way to
go about this.

Note that the point of this file adds new primes and composites each time
a new one is found.
'''

primes = []

maxPrime = -1


def initialize():
	global compositeFLink
	global composites
	global maxComposites
	global primeFLink
	global primes
	global maxPrime

	##############################################################################
	# Make composite numbers
	##############################################################################

	compositeFLink = open("composites_1000000.txt","ra")

	nums = []
	composition = []

	appendToNums = nums.append
	appendToComposition = composition.append

	for line in compositeFLink :

		text = line.split()

		appendToNums(int( text[0] ))

		tempComposition = [ int(item) for item in text[2:] if '*' not in item  ]

		appendToComposition(tempComposition)

	composites = dict( zip(nums,composition)  )

	maxComposites = max(nums)

	##############################################################################
	# Make primes
	##############################################################################

	primeFLink = open("primes1.txt",'ra')

	appendToPrimes = primes.append

	for line in primeFLink :

		text = line.split()

		for item in text:

			appendToPrimes(int(item))

	maxPrime = max(primes)

	primes = set(primes)

def isPrime(nn , shouldWrite2File = True):
	'''
	Test if the input number is a prime number

	if so but not recorded, then updates set

	Will not update composite number dictionary if input 
	number is not prime
	'''
	global composites
	global maxComposites

	if nn == 1 :
		return False

	if nn in primes:
		return True

	if nn in composites:
		return False

	ii = 2

	while ii**2 <= nn :
		if nn%ii == 0 :
			return False

	if shouldWrite2File :
		textToAdd = "%d\n" % nn
		primeFLink.write(textToAdd)

	primes.add(nn)

	if maxPrime <= nn :
		maxPrime = nn

	return True

def isCompsite(nn , shouldWrite2File = True ):
	'''
	Test if the input number is a composite number

	if so but not recorded, then updates dictionary

	Will not update prime number set if input number is prime
	'''

	global composites
	global maxComposites

	if nn == 1 :
		return False

	if nn in composites:
		return True

	if nn in primes:
		return False

	isTrue = False

	compositionList = []

	ii = 2

	tempNum = nn

	while tempNum > 1 :
		if tempNum % ii == 0 :
			tempNum /= ii
			compositionList.append(ii)
		else:
			ii += 1

	if len(compositionList) > 1 :
		# Then not a prime number

		# add new element
		composites[nn] = compositionList

		if shouldWrite2File:
			compositionText = "%d * "*( len(compositionList) - 1 )

			compositionText+= "%d" 

			copositionText = compositionText % tuple(compositonList)

			textToAdd = " %d = %s \n" %( nn , copositionText )

			compositeFLink.write( textToAdd )

		if maxComposites <= nn :
			maxComposites = nn

		isTrue =  True
	else:
		isTrue = False

	return isTrue

initialize()
