import stupidPi

def arctanInt(pp,qq,dd) :
	'''
	Takes in two ints pp and qq that represent a rational representstion
	of the value x in which we want to calcualte arctan for.

	x = p/q

	returns arctan(x) multiplied by 10^dd as an int
	'''
	count   = 0
	total   = 0
	product = 10**dd * pp / qq    
	term    = product          # next term to add
	while abs(term) > 0:
		count +=1
		total += term

		product *= -pp**2 
		product /=  qq**2
		
		term = product / (2* count +1)

	return total


def calcPi( digits ):
	'''
	Calculates :

	pi = 16 arctan(1/5) - 4 arctan(1/239)

	This calculates pi in reasonable time to the number of digits specified
	'''
	
	dd = 10**digits

	aa = arctanInt(1,  5,digits)
	bb = arctanInt(1,239,digits)

	value =  16*aa - 4*bb

	return (value/dd , value %dd )

def calcNumDigits(bigNum):
	count = 0

	while abs(bigNum) > 0 :

		bigNum /= 10
		count  += 1

	return count

def displayPi(digits):

	pi = calcPi(digits)

	print "Calculated Pi"
	print "pi ~= %d.%d"%pi
	print ""

	'''
	diffDD = stupidPi.piDigits - digits

	if diffDD > 0 :

		massPi = stupidPi.pi[1] / 10**diffDD

		print "Real Pi"
		print "pi ~= %d.%d"%(3,massPi)
		print ""
		print "difference = %d x 10^(%+d)"%(massPi-pi[1],-digits)
	'''
	
	diffDD = stupidPi.bigPiDigits - digits

	if diffDD > 0 :
		massPi = stupidPi.bigPi[1] / 10**diffDD
		print "Real Pi"
		print "pi ~= %d.%d"%(3,massPi)
		print ""
		print "difference = %d x 10^(%+d)"%(massPi-pi[1],-digits)


displayPi(10000)