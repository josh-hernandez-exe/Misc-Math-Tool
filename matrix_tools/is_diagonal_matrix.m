function isTrue = is_diagonal_matrix(M)
% Purpose:
%   Checks to see if passed matrix is diagonal
%
% Def:
%   A diagonal matrix is one where M(i,i)=0 for all i and
%   M(i,j) ~= 0  for i~=j 
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is diagonal
%
    isTrue = false;

    if is_square_matrix(M)
        isTrue = ~any(any( M-diag(diag(M)) ));
    end
end