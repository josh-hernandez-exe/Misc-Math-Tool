
import numpy as np
import time

DEBUG = False

def integrateSimpson( func, aa,bb , nn ):
	'''
	This function will use Simpson's 1/3 method to
	approximate the integral of a function.
	
	Input :
		func = reference to a one variable function
		aa   = the left-most integration limit
		bb   = the right-most integration limit
		nn   = the number of sub-intervals
	
	Output :
		total = aproximated value for the integral
	'''
	
	(xVals,yVals,hh) = processData( func, aa,bb ,nn )
	
	if (nn%2)!=0 :
		print 'The number of subintervalse must be a multiple by 2'
		raise
		
	total =    yVals[0] + yVals[nn]
	total+=  4*np.sum( yVals[1:nn:2] )
	total+=  2*np.sum( yVals[2:nn:2] )
	
	total*= hh/3.0
	
	return total


def integrateTrap( func, aa,bb , nn ):
	'''
	This function will use Simpson's 1/3 method to
	approximate the integral of a function.
	
	Input :
		func = reference to a one variable function
		aa   = the left-most integration limit
		bb   = the right-most integration limit
		nn   = the number of sub-intervals
	
	Output :
		total = aproximated value for the integral
	'''
	(xVals,yVals,hh) = processData( func, aa,bb ,nn )
	
	total =  ( yVals[0] + yVals[nn]) / 2
	total+= np.sum( yVals[1:nn] )
	
	total*= hh
	
	return total

def processData( func, aa,bb, nn):
	'''
	This function will take in the parameter passed to a numerical integrator to
	validate and process the data.
	
	Output:
		xVals = x values in the interval [aa,bb] that are uniformly spaced
		yVals = y values of the function at the specified x values
		hh    = step size
	'''
	
	if not callable(func) :
		print "The first vairable must be callable (hopfully a function)"
		raise
	
	if aa > bb :
	
		aa,bb = bb,aa
	
	if nn <= 0 :
		print "The number of subintervals must be positive"
		raise

	xVals = np.linspace(aa,bb,nn+1)
	
	yVals = func(xVals)
	
	hh = xVals[1]-xVals[0]
	
	return (xVals,yVals,hh)


def calcRelError(yy,y_true):
	'''
	This function calculates the relative error between the approximated solution and the
	analytic solution
	'''
	return ( yy - y_true )*100.0/y_true