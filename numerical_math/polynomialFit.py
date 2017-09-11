import numpy as np
from collections import defaultdict

def least_squares_poly_fit(xx,yy,kk):
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

    yy = np.matrix(yy).reshape(len(yy),1)

    temp_m = MM.transpose() * MM

    params = temp_m**(-1) *  MM.transpose() * yy

    params = np.array(params).flatten()

    return params

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
    array_check = isinstance(x_val,np.ndarray)

    if reverse:
        poly_coef = poly_coef[::-1]

    y_val = None
    if num_check and not array_check:
        y_val = 0

    elif array_check:
        y_val = np.zeros( x_val.shape )
    else:
        raise "Error"

    for coef_val in poly_coef:
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

    iterator = zip(input_y_vals[:-1],input_y_vals[1:],spline_vals[:-1],spline_vals[1:])

    for yy_i,yy_ip1,dd_i,dd_ip1 in iterator:
        # polynomial coefs
        # y(t) = a + bt + ct^2 + dt^3
        # aa = yy_i
        # bb = dd_i
        cc = 3*(yy_ip1 - yy_i) - 2*dd_i - dd_ip1
        dd = 2*(yy_i - yy_ip1) + dd_i + dd_ip1

        coef_list.append((yy_i,dd_i,cc,dd))

    return coef_list

def calc_spline_interpolation(output_x_vals, input_y_vals, dtype = np.float):
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

    output_y_vals = np.zeros(len(output_x_vals), dtype=dtype)

    xvals_per_poly = defaultdict(list)
    index_mapping_per_poly = defaultdict(list)

    for index,x_val in enumerate(output_x_vals):
        poly_index = int(x_val)
        if poly_index == len(coef_list):
            # the edge of the final polynomial
            poly_index -= 1
        xvals_per_poly[poly_index].append(x_val - poly_index)
        index_mapping_per_poly[poly_index].append(index)

    for poly_index in xvals_per_poly:
        x_vals = np.array(xvals_per_poly[poly_index])
        y_vals = calc_poly(x_vals,coef_list[poly_index],reverse=True)
        mask = np.array(index_mapping_per_poly[poly_index])
        output_y_vals[mask] = y_vals

    return output_y_vals

if __name__ == "__main__":
    print('LEAST SQUARES REGRESSION TEST')
    aa = range(10)
    bb = range(10)
    cc = least_squares_poly_fit(aa, bb, 4)
    print(aa)
    print(bb)
    print(cc)

    print('CUBLIC SPLINE TESTS')

    aa = np.linspace(0,5,20)
    bb = range(10)
    cc = calc_spline_interpolation(np.linspace(0,5,20), bb)

    print(aa)
    print(bb)
    print(cc)

    bb = range(10)
    aa = np.linspace(bb[-3],bb[-1],20)
    cc = calc_spline_interpolation(np.linspace(0,5,20), bb)

    print(aa)
    print(bb)
    print(cc)


    aa = np.linspace(0,5,20)
    bb = np.random.random(10)
    cc = calc_spline_interpolation(np.linspace(0,5,20), bb)

    print(aa)
    print(bb)
    print(cc)
