import numpy as np

def leastSquaresPolyFit(xx,yy,kk):
    '''
    Applies Least Squares regression on the data do create
    the coefficient of a polynomial of degree k
    '''
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

def calc_poly(x_val,poly_coef,reverse=False):

    num_check = isinstance(x_val, (int,float,complex, np.number))

    if reverse:
        polyCoef = polyCoef[::-1]

    y_val = None
    if num_check and not isinstance(x_val,np.ndarray):
        y_val = 0

    elif isinstance(x_val,np.ndarray) :
        y_val = np.zeros( x_val.shape )
    else:
        raise "Error"

    for coef_val in np.nditer(polyCoef):
        # calculates
        # yFit = aa*xVal**n + bb*xVal**(n-1) + ...
        # faster
        y_val *= x_val
        y_val += coef_val

    return y_val


# CUBLIC SPLINE INTERPOLATION

def _make_cubic_spline_matrix(nn):
    ii = np.eye(nn,nn)
    sub_ii = np.tri(nn,nn,k=-1) - np.tri(nn,nn,k=-2)

    coeff = 4*ii + sub_ii + sub_ii.transpose()

    coeff[0][0] = 2
    coeff[nn-1][nn-1] = 2

    return np.matrix(coeff)

def _make_cubic_spline_vector(y_vals):
    temp_1 = np.array(list(y_vals[1:]) + [y_vals[-1]])
    temp_2 = np.array([y_vals[0]] + list(y_vals[:-1]))
    vv =  3*(temp_1-temp_2)
    vv = vv.reshape([len(vv),1])

    return np.matrix(vv)

def _generate_cubic_spline_coef_list(input_y_vals, spline_vals):
    coef_list = []

    for ii in range(len(input_y_vals)-1):
        yy_i = input_y_vals[ii]
        yy_ip1 = input_y_vals[ii+1]
        dd_i = spline_vals[ii]
        dd_ip1 = spline_vals[ii+1]

        # polynomial coefs
        # y(t) = a + bt + ct^2 + dt^3
        aa = yy_i
        bb = dd_i
        cc = 3*(yy_ip1 - yy_i) - 2*dd_i - dd
        dd = 2*(yy_i - yy_ip1) + dd + dd_ip1

        coef_list.append((aa,bb,cc,dd))

    return coef_list

def calc_spline_interpolation(output_x_vals, input_y_vals):
    """
    the input_y_vals are expected to be evenly spaced.
    where the input_x_vals are the integers from 0.

    """

    matrix_coef = _make_cubic_spline_matrix(len(input_y_vals))
    vector = _make_cubic_spline_vector(input_y_vals)

    spline_vals = matrix_coef**(-1) * vector
    spline_vals = np.array(spline_vals).flatten()

    assert len(input_y_vals) == len(spline_vals)

    # generate each set of coefficents for each piecewise polynomials
    # note that the number of polynomicals is one less than the total number of points
    coef_list = _generate_cubic_spline_coef_list(input_y_vals, spline_vals)

    # calculate a map of which polynomial to use
    poly_map = [ int(xx) for xx in output_x_vals]

    output_y_vals = []

    for ii in range(len(output_x_vals)):
        poly_index = int(output_x_vals[ii])
        xx = output_x_vals[ii] - poly_index
        yy = calc_poly(xx,poly_map[poly_index],reverse=False)
        output_y_vals.append(yy)

    return np.array(output_y_vals)
