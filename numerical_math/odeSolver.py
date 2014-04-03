import numpy as np
import time

DEBUG = False

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

def odeEulers(dy,t_0,t_f,y_0,hh):
	'''
	This funciton applies Eulers method to solving an ODE
	
	Input :
		dy  = function handle to the RHS of the ode
		t_0 = initial time value
		t_f = final time value
		y_0 = initial solution vector ( occuring at time t_0)
		hh  = time step
	
	Output:
		tt = vector of time values
		yy = an array of values, where yy[:,i] is a vector approximating the solution at tt[ii]
	'''
	
	(tt,yy,nn) = validateData(dy,t_0,t_f,y_0,hh)
	
	for ii in range(nn-1):
	
		yy[:,ii+1] = yy[:,ii] + hh*dy( tt[ii],yy[:,ii] );

	return (tt,yy)

def odeNystrams(dy,t_0,t_f,y_0,hh):
	'''
	This funciton applies Nystrams method to solving an ODE. This particular
	implementation uses RK4 as the kickstarting method.
	
	Input :
		dy  = function handle to the RHS of the ode
		t_0 = initial time value
		t_f = final time value
		y_0 = initial solution vector ( occuring at time t_0)
		hh  = time step
	
	Output:
		tt = vector of time values
		yy = an array of values, where yy[:,i] is a vector approximating the solution at tt[ii]
	'''
	
	(tt,yy,nn) = validateData(dy,t_0,t_f,y_0,hh)
	
	# kickstart with RK4
	yy[:,1] = RK4_kickstarter(dy,tt,y_0,hh)
	
	for ii in range(1,nn-1):
	
		yy[:,ii+1] = yy[:,ii-1] + 2*hh*dy( tt[ii],yy[:,ii] );

	return (tt,yy)

def odeHuens(dy,t_0,t_f,y_0,hh):
	'''
	This funciton applies Huens method to solving an ODE
	
	Input :
		dy  = function handle to the RHS of the ode
		t_0 = initial time value
		t_f = final time value
		y_0 = initial solution vector ( occuring at time t_0)
		hh  = time step
	
	Output:
		tt = vector of time values
		yy = an array of values, where yy[:,i] is a vector approximating the solution at tt[ii]
	'''
	
	(tt,yy,nn) = validateData(dy,t_0,t_f,y_0,hh)

	for ii in range(nn-1):
		
		K1 = dy( tt[ii]   , yy[:,ii]         )
		K2 = dy( tt[ii+1] , yy[:,ii] + hh*K1 )
		
		yy[:,ii+1] = yy[:,ii] + hh*(K1+K2)/2;

	return (tt,yy)

def RK4_kickstarter(dy,tt,yy,hh):
	'''
	This funciton applies RK4 method to solving an ODE for one time step.
	This function is used to kickstart other ODE solvers that cannot self start.
	
	Input :
		dy  = function handle to the RHS of the ode
		tt  = current time value
		yy  = current solution vector
		hh  = time step
	
	Output:
		yy =  vector approximating the solution at tt+hh
	'''
	
	K1 = dy( tt        , yy         );
	K2 = dy( tt+0.5*hh , yy+K1*hh/2 );
	K3 = dy( tt+0.5*hh , yy+K2*hh/2 );
	K4 = dy( tt+hh     , yy+K3*hh  );
	
	yy = yy + (K1 + 2*K2 + 2*K3 + K4)*hh/6;
	
	return yy

def odeRK4(dy,t_0,t_f,y_0,hh):
	'''
	Forth order Runge-Kutta
	
	NOTE: If input are vectors (i.e. for a system of ODE's)
	       They must be given as column vectors
	       
	Input :
		dy  = function handle to the RHS of the ode
		t_0 = initial time value
		t_f = final time value
		y_0 = initial solution vector ( occuring at time t_0)
		hh  = time step
	
	Output:
		tt = vector of time values
		yy = an array of values, where yy[:,i] is a vector approximating the solution at tt[ii]
	'''
	
	(tt,yy,nn) = validateData(dy,t_0,t_f,y_0,hh)
	
	
	for ii in range(nn-1):
	
		K1 = dy( tt[ii]        , yy[:,ii]         );
		K2 = dy( tt[ii]+0.5*hh , yy[:,ii]+K1*hh/2 );
		K3 = dy( tt[ii]+0.5*hh , yy[:,ii]+K2*hh/2 );
		K4 = dy( tt[ii+1]      , yy[:,ii]+K3*hh  );
		
		yy[:,ii+1] = yy[:,ii] + (K1 + 2*K2 + 2*K3 + K4)*hh/6;

	return (tt,yy)

def validateData(dy,t_0,t_f,y_0,hh):
	'''
	This function checks that the parameters given to the ODE solvers
	are valid. Also this function will calculate the time and y-vectors
	based on the data types that are passed.
	'''
	
	if not callable(dy) :
		print "The first vairable must be callable (hopfully a function)"
		raise
	
	if(t_f < t_0) :
		t_0,t_f = t_f,t_0
	
	if hh < 0 :
		print "The step size must be positive"
		raise

	# test that y_0 is a vector
	
	if isinstance(y_0,np.ndarray):
		pass
	else:
		if isinstance(y_0,list) or isinstance(y_0,tuple):
			y_0 = np.array(y_0)#,dtype = np.float64)
		else:
			y_0 = np.array([y_0])#,dtype = np.float64)
	
	tt = arrayRange(t_0,t_f+hh/2,hh)
	
	nn = len(tt);
	
	mm = len(y_0);
	
	yy = np.zeros([mm,nn]);
	
	yy[:,0] = y_0;
	
	return (tt,yy,nn)

def calcRelError(xx,yy,x_0,y_0,y_sol):
	'''
	This function calculates the relative error between the approximated solution and the
	analytic solution
	'''
	y_true = y_sol(xx,x_0,y_0)
	return ( yy - y_true )*100/y_true

def vanderPol(tt,rr,gamma):
	'''
	Vander Pol Oscillator (unforced)
	
	xddot - gamma*(1-x^2)*xdot + x = 0
	
	u = x
	v = xdot
	
	udot = v
	vdot = gamma(1-u^2)*v-u
	'''
	uu = rr[0]
	vv = rr[1]
	
	dy = 0.0*rr
	
	dy[0] = vv
	dy[1] = gamma*(1-uu**2)*vv - uu

	return dy

def duffingEquation(tt,rr,alpha):
	'''
	Vander Pol Oscillator (unforced)
	
	xddot + alpha_1*xdot-alpha_2*x + alpha_3*x^3 = 0
	
	u = x
	v = xdot
	
	udot = v
	vdot = gamma(1-u^2)*v-u
	'''
	
	uu = rr[0]
	vv = rr[1]
	
	dy = 0.0*rr
	
	dy[0] = vv
	dy[1] = -alpha[0]*vv - alpha[1]*uu - alpha[2]*uu**3

	return dy