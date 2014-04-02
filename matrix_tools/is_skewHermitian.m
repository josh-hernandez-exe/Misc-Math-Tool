function isTrue = is_skewHermitian(M)
% Purpose:
%   Checks to see is the matrix is anti-Hermitian (if complex matrix)
%   or symmetrix ( if real matrix )
% 
% Definition:
%   anti-Hermitian : M = - M^*  <-- conjugate transpose
%   anti-Symmetrix : M = - M^T  <-- Transpose
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is anti-Hermitian
%
    isTrue = is_anti_hermitian_matrix(M);
end