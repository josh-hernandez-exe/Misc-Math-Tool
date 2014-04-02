function isTrue = is_real_matrix(M)
% Purpose:
%   Checks to see if passed matrix has at no complex entrys
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean relating if matrix is real and not complex
%
    isTrue = false;
        
    if is_matrix(M)
        isTrue = all(all( imag(M)==0 ));
    end
end