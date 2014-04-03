import numpy as np

DEBUG = False

def diff2ptForward(xx,yy,tol = 10**(-6)):
	'''
	The 2-point forward difference method
	
	Input :
		xx  = x values of the data
		yy  = y values of the data corresponding to the x values
		tol = optinal tolerence check for comparing uniform spacing
	
	Output :
		xx[index] = x values corresponding to the calcualted points of the derivative
		dy        = approximated derivative points
	'''
	
	(nn,hh) = validateData(xx, yy,tol)
	
	index=np.arange(0,nn-1)
	
	dy = yy[index+1]-yy[index]
	
	dy /= hh;
	
	return (xx[index],dy)

def diff2ptCenter(xx,yy,tol = 10**(-6)) :
	'''
	The 2-point center difference method
	
	Input :
		xx  = x values of the data
		yy  = y values of the data corresponding to the x values
		tol = optinal tolerence check for comparing uniform spacing
	
	Output :
		xx[index] = x values corresponding to the calcualted points of the derivative
		dy        = approximated derivative points
	'''
	
	(nn,hh) = validateData(xx,yy,tol)
	
	index=np.arange(1,nn-1)
	
	dy = yy[index+1]-yy[index-1]
	
	dy /= 2*hh;
	
	return (xx[index],dy)



def validateData( xVals, yVals ,tol = 10**(-6)) :
	'''
	This function validates the data that would be passed to any of the
	numerical derivative fucntions. This function will also calculate the
	step size assuming uniform step sizes.
	'''
	
	if not ( isinstance(xVals,np.ndarray) and isinstance(yVals,np.ndarray) ):
		print "The first two parameters must be an instance of numpy.ndarray"
		raise

	numDataPoints = len(yVals)

	nn = numDataPoints - 1

	assert len(xVals) == numDataPoints , 'Must have the same number of data point'
	
	assert numDataPoints > 1 , 'Must have at least two data points to calcuate the integral'
	
	hh = abs(xVals[1] - xVals[0])

	if numDataPoints > 1 :
		if np.any( np.abs( np.abs(  xVals[0:(nn-1)]-xVals[1:nn]  ) - hh) > tol ):
			print 'This function assumes that data is equally spaced'
			raise

	return (numDataPoints,hh)


def arrayRange(start,stop,step):
	'''
	This function works very similarly to the function arange in
	the numpy library. There are a few more calculations for accuracy.
	This way linspace doesn't need to be used.
	'''
	xx = np.arange(start,stop,step)
	
	xx/= step
	
	xx = np.round(xx)
	xx = np.array(xx,dtype = np.int32)
	
	return xx*step


def convertToStr(xx):
	'''
	This is really a debuging fuction. Used to convert arrays in
	string for the purpose of being displayed neatly.
	'''
	textModifier = "%5.2f "*len(xx)
	
	textModifier = "[ "+textModifier+" ]"
	
	return textModifier % tuple(xx)