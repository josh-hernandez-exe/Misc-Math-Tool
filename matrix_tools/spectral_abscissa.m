function s_of_M = spectral_abscissa(M)
% Purpose:
%   Calculates the spectral abscissa of M and returns it. This is
%   determined by using the following definition.
%
% Def:
%   spectral abscissa of M denoted s(M) is
%   s(M) = max( real(lambda) | lambda in spectrum of M  )
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   s_of_M = the spectral abcissa of M
%
    s_of_M = NaN;

    if is_square_matrix(M)
        
        lambda = eig(M);

        s_of_M = max(real(lambda));      
    else
        disp('There is no spectral abscissa since matrix is not square.');
    end
end