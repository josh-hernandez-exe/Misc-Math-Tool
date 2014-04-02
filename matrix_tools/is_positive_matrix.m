function isTrue = is_positive_matrix(M)
% Purpose:
%   Checks to see if the passed matrix satisfies the definition of
%   a positive matrix. There are two definitions implamented. Only
%   one should be used.
%
%   def1,def2 are embedded functions that are used to implament the
%   two definitions
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is positive
%
    isTrue = def_1(M);
    %isTrue = def_2(M);
    
end

function isTrue = def_1(M)
% Purpose:
%   Checks to see if the passed matrix satisfies the definition of
%   a positive matrix with the following definition
%
% Def:
%   M(i,j)> 0 for any i,j
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is positive
%
    isTrue = false;
        
    if is_matrix(M)   
        isTrue = all(all( M > 0 ));
    end   
end

function isTrue = def_2(M)
% Purpose:
%   Checks to see if the passed matrix satisfies the definition of
%   a positive matrix with the following definition
%
% Def:
%   M(i,j)>= 0 for any i,j and there exsist ii,jj such that M(ii,jj) > 0
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is positive
%
    isTrue = false;

    if is_matrix(M)      
        isTrue = all(all(M >= 0)) && any(any( M > 0 ))  ;        
    end   
end