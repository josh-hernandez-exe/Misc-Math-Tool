function isTrue = is_unitary_matrix(M)
% Purpose:
%   Checks to see is the matrix is unitary (if complex matrix)
%   or orthognal ( if real matrix )
% 
% Definition:
%   Unitary    : M * (M^*) = I   <-- conjugate transpose
%   Orthogonal : M * (M^T) = I   <-- Transpose
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is unitary
%
    isTrue = false;

    if is_square_matrix(M)
        isTrue = all(   all(  abs(M*(M')-eye( size(M)))<tol    ));
    end
end