function force_square_matrix(M)
% Purpose:
%   Checks to see if the passed matrix is square.
%    If not, an error is raised.      
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   Nothing
%

    if ~is_square_matrix(M)
        error('Matrix given is not square. Please enter a square matrix.');
    end

end