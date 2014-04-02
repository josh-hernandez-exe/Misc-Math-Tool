function isTrue = is_normal_matrix(M)
% Purpose:
%   Checks to see if the matrix passed is normal by the following
%   definition.
%
% Def:
%   A square matrix is normal if M and it's congugate-transpose commute
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean representing if the matrix is normal
%
    isTrue = false;

    if is_square_matrix(M)
        isTrue = all(all((M*M')==(M'*M)));
    end
end