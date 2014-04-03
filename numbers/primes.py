'''
http://primes.utm.edu/lists/small/millions/

The first million primes
first : 2
last  :15,485,863
'''

primes = []

maxPrime = -1

'''
productDistinctPrimes = []

appendToProduct = productDistinctPrimes.append

for ii in range(len(primes)):
	for jj in primes[ii:]:

		value = primes[ii] * jj

		if value not in productDistinctPrimes :
			appendToProduct(value)

del appendToProduct
del ii,jj

productDistinctPrimes = set(productDistinctPrimes)
'''

def initialize():
	global flink
	global primes
	global maxPrime

	flink = open("primes1.txt",'ra')

	appendToPrimes = primes.append

	for line in flink :

		text = line.split()

		for item in text:

			appendToPrimes(int(item))

	maxPrime = max(primes)

	primes = set(primes)

def isPrime(nn , shouldWrite2File = True):

	global composites
	global maxComposites

	if nn in primes:
		return True

	ii = 2

	while ii**2 <= nn :

		if nn%ii == 0 :
			return False

	if shouldWrite2File :
		flink.write(nn)

	primes.add(nn)

	if maxPrime <= nn :
		maxPrime = nn

	return True


initialize()