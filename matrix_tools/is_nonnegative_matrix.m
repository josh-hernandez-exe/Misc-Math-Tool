function isTrue = is_nonnegative_matrix(M)
% Purpose:
%   Checks to see if the passed matrix satisfies the definition of
%   a is_nonnegative matrix, with the following defintion.
%
% Def:
%   M(i,j)>= 0 for any i,j
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is is_nonnegative
%
    isTrue = true;      
    if is_matrix(M)
        
        isTrue = all(all(M >= 0));      
    end     
end