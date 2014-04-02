function plot_spectral_radius(M)
% Purpose:
%   To plot the the circle that contains all the eigenvalues of the passed
%   matrix on the complex plane. This finds the spectral radius and plots a
%   circle of that radius centered at the origin. It is plotted it '.' for
%   a bolding effect.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   Nothing
%
    hold on
    
    if is_square_matrix(M)
        
        sRadius = spectral_radius(M);
        
        [x,y] = circle_for_plot(0,0,sRadius);
        
        plot(x,y,'.');
        
    else
        disp('There are no eigenvalues since matrix is not square.');
    end

end