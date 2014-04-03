import numpy as np

def leastSquaresPolyFit(xx,yy,kk):
	nn = len(xx)
	MM = np.ones([nn,kk+1])

	xx = np.matrix(xx)
	xx = xx.transpose()
	xx = np.array(xx)

	MM[:,kk-1] = xx[:,0]

	for jj in range(kk-1,-1,-1):
		# loop backwards from k-1 to 0 
		MM[:,jj] = xx[:,0]*MM[:,jj+1]

	MM = np.matrix(MM)

	yy = np.matrix(yy)
	yy = yy.transpose()

	tempM = MM.transpose() * MM

	params = tempM**(-1) *  MM.transpose() * yy 

	params = params.transpose()
	params = np.array(params)

	return params[0] # an odd fix to cast to 1-D array

def lagrangePoly(xval,xList,yList):

	numCheck = type(xval)==int or type(xval)==float
	numCheck = numCheck or type(xval)==complex
	numCheck = numCheck or isinstance(xval, np.number)

	listCheck = type(xval) == list or type(xval)==tuple 
	listCheck = listCheck or isinstance(xval,np.ndarray)

	if numCheck and not listCheck :
		nn = len(xList)
		xList = np.array(xList)
		lagrangeList = np.zeros(nn)
		for ii in range(nn):
			lagrangeList[ii] = lagrangePolyHelper(xval,xList,ii)

		yVal = np.sum( yList * lagrangeList )

		return yVal

	elif isinstance(xval,np.ndarray) and not numCheck :
		print xval
		yVals = np.zeros( xval.shape )

		for ii in range(xval.size) :
			yVals[ii] = lagrangePoly(xval[ii],xList,yList)

		return yVals

	elif type(xval) == list or type(xval)==tuple  :

		return lagrangePoly(np.array(xval),xList,yList)

	else :
		# nothing should get here
		pass

def lagrangePolyHelper(xval,xList,ii):

	denom = xList[ii] - xList
	denom[ii]=1

	numer = xval - xList
	numer[ii]=1

	# I set the entries to 1 so that they do not affect the product
	yVal = np.prod(numer)/float(np.prod(denom))

	return yVal

def calcPoly(xVal,polyCoef,reverse=False):

	numCheck = type(xVal)==int or type(xVal)==float
	numCheck = numCheck or type(xVal)==complex
	numCheck = numCheck or isinstance(xVal, np.number)

	if reverse:
		polyCoef = polyCoef[::-1]


	if numCheck and not isinstance(xVal,np.ndarray) :
		yVal = 0

	elif isinstance(xVal,np.ndarray) :
		yVal = np.zeros( xVal.shape )

	else:
		raise "Error"	

	for coefVal in np.nditer(polyCoef):
		# calculates 
		# yFit = aa*xVal**n + bb*xVal**(n-1) + ...
		# faster
		yVal *= xVal 
		yVal += coefVal

	return yVal