import primes as p
'''
http://www.naturalnumbers.org/composites.html
'''

def initialize():
	global flink
	global composites
	global maxComposites

	flink = open("composites_1000000.txt","ra")

	nums = []
	composition = []

	appendToNums = nums.append
	appendToComposition = composition.append

	for line in flink :

		text = line.split()

		appendToNums(int( text[0] ))

		tempComposition = [ int(item) for item in text[2:] if '*' not in item  ]

		appendToComposition(tempComposition)

	composites = dict( zip(nums,composition)  )

	maxComposites = max(nums)

def isCompsite(nn , shouldWrite2File = True ):

	global composites
	global maxComposites

	if not isPrime(nn) :

		compositionList = []

		ii = 2

		while nn > 1 :

			if nn % ii == 0 :

				nn /= ii

				compositionList.append(ii)

			else:
				ii += 1

		# add new element
		composites[nn] = compositionList

		if shouldWrite2File:
			compositionText = "%d * "*( len(compositionList) - 1 )

			compositionText+= "%d" 

			copositionText = compositionText % tuple(compositonList)

			textToAdd = " %d = %s " %( nn , copositionText )

			flink.write( textToAdd )

		if maxComposites <= nn :
			maxComposites = nn

initialize()