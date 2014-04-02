function plot_all_eigenvalues(M)
% Purpose:
%   Takes the passed matrix and plots the eigenvalues, treating the graph
%   as the complex plane.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   Nothing
%
    if is_square_matrix(M)
        
        lambda = eig(M);
        
        hold on
        
        for i=1:length(lambda)
            plot(real(lambda(i)),imag(lambda(i)),'r*')
        end
        
    else
        disp('There are no eigenvalues since matrix is not square.');
    end
end