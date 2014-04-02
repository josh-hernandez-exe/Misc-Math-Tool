function sRadius = spectral_radius(M)
% Purpose:
%   Calculates the spectral radius of M and returns it. This is
%   determined by using the following definition.
%
% Def:
%   spectral radius of M the maximum of the magnitudes of all the
%   eigenvalues of M.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   sRadius = the spectral radius of M
%
    sRadius = NaN;

    if is_square_matrix(M)
        
        lambda = eig(M);

        sRadius = max(abs(lambda));
    end
end