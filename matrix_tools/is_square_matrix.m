function isTrue = is_square_matrix(M)
% Purpose:
%   Checks to see if the passed matrix is square. This is done by looking
%   a the size vector of M. If both entries are the same then each
%   dimension of the array is the same value. We take this to be a square
%   matrix.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean value representing if the matrix is square
%
    sizes = size(M);

    isTrue = false;

    if is_matrix(M)
        if sizes(1)==sizes(2)
           isTrue = true ;
        end
    end
end