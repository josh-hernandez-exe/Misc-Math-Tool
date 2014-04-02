function isTrue = is_unitary(M)
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
    isTrue = is_unitary_matrix(M);
end