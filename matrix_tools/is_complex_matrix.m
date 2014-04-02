function isTrue = is_complex_matrix(M)
% Purpose:
%   Checks to see if passed matrix has at least one complex entry
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is complex
%
    isTrue = false;
        
    if is_matrix(M)
        isTrue = any(any( imag(M)~=0 ));
    end
end