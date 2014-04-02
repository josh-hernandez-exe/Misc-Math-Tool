function isTrue = is_Hermitian(M)
% Purpose:
%   Checks to see is the matrix is Hermitian (if complex matrix)
%   or symmetrix ( if real matrix )
% 
% Definition:
%   Hermitian : M = M*   <-- conjugate transpose
%   Symmetrix : M = M^T  <-- Transpose
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is Hermitian
%
    isTrue = is_hermitian_matrix(M);
end