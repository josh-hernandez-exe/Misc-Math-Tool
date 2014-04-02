function bound = bounds_spectral_radius(M)
% Purpose:
%   Provides the bounds on the spectral radius of M given by row sums.  
%
% Input :            
%   M = Matrix of float (real or complex) values
%
% Returns :
%   bound = a float the bound of the spectal radius
%           returns NaN if matrix is not square
%

    bound = NaN;
    
    if is_square_matrix(M)
        
        % note that sum(M) returns a vector of coloumn sums
        % so sum(M') is a vector of row sums
        
        bound = max( sum( abs( M' ) ) );
        
    else
        disp('There are no bounds on the spectral radius since matrix is not square.');
    end

end