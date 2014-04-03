import numpy as np

DEBUG = False

def newtonsMethod( ff , dff , x0 , tol = 10**(-2) ,maxIter = 10**4):
	

	if not ( callable(ff) and callable(dff) ):
		raise "The function and the derivative function must be passed and be callable."

	xx = x0

	isFirstRun = True

	xOld = xx
	
	count = 0

	while (abs(xx-xOld) >= tol or isFirstRun) and count <= maxIter :

		xOld = xx

		xx = xx - ff(xx)/dff(xx)


		if DEBUG and isFirstRun:

			print ''
			print 'Newton s Method'
			print 'iter       xi        f(xi)       df(xi)        '

		if DEBUG :
			print '%3d %11.6f %11.6f %11.6f\n'%(count,xx,ff(xx),dff(xx))


		isFirstRun = False
		count+=1

	return xx


def bisectionMethod(ff,aa,bb,tol=0.0001,maxIter=10**4):

	if not callable(ff) :
		raise "The function passed must be passed and be callable."

	if aa>bb :
	   aa,bb = bb,aa
	
	if ff(a)*ff(b) > 0 :
		raise 'Error: endpoints have the same sign'

	isFirstRun = True
	
	count = 0

	while (isFirstRun or fxi >= tol) and count <= maxIter :

		xi = 0.5*(aa+bb)

		toli = (bb-aa)/2
		 
		fxi = ff(xi)

		if f(a)*fxi < 0 :
			bb= xi
		else :
			aa= xi


		if DEBUG and isFirstRun:

			print ''
			print 'Bisection Method'
			print 'iter       a           b         f(a)        f(b)         xi         f(xi)        tol'

		if DEBUG :
			print '%3d %11.6f %11.6f %11.6f %11.6f %11.6f %11.6f %11.6f\n'%(count,aa,bb,ff(aa),ff(bb),xi,fxi,toli)

		isFirstRun = False
		count+=1

	return xi


def secentMethod(ff,aa,bb,tol=0.0001,maxIter=10**4):
	
	if not callable(ff) :
		raise "The function passed must be passed and be callable."

	if aa>bb :
	   aa,bb = bb,aa

	x1 = aa
	x2 = bb

	for ii in range(maxIter) :

		fx1 = ff(x1)

		fx2 = ff(x2)

		xi = x2 - fx2 * (x1-x2) / (fx1-fx2) 

		if DEBUG and isFirstRun:
			print ''
			print 'Secant Method'
			print 'iter      x1         f(x1)        x2          f(x2)        xi'

		if DEBUG :
			print '%3d %11.6f %11.6f %11.6f %11.6f %11.6f\n' % (ii,x1,fx1,x2,fx2,xi)

		x1 = x2
		x2 = xi

	return xi









