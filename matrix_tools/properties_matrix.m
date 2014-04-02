function properties_matrix(M)
% Purpose:
%   Given the passed matrix, any information that can be concluded about
%   the matrix will be displayed. Also the eigenvalues, Gershporin Disks,
%   spectral circle will be plotted by treating the graph as the complex
%   plane.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   Nothing
%
    fprintf('\n');

    if is_matrix(M)
        
        fprintf('Matix = \n');
        disp(M);
        
        isReal = is_real_matrix(M);
        
        if isReal
            disp('Matrix is made of real entries');
        else
            disp('Matrix is made of complex entries');
        end
        
        if is_positive_matrix(M)
            disp('Matrix is positive');
        elseif is_nonnegative_matrix(M)
            disp('Matrix is non-negative');
        end
        
        if is_square_matrix(M)
            
            isIrreducible = is_irreducible_matrix(M);
            determinate = det(M);
            [eVector,eValue] = eig(M);
            
            disp('Matrix is square');

            if is_diagonal_matrix(M) 
                disp('Matrix is diagonal');
            elseif is_upper_triagular_matrix(M)
                disp('Matrix is upper triagular');
            elseif is_lower_triagular_matrix(M)
                disp('Matrix is lower triagular');
            end            
            
            if is_primitive_matrix(M) 
                disp('Matrix is primitive');
            else
                disp('Matrix is imprimitive');
            end
            
            if isIrreducible
                disp('Matrix is irreducible');
                
            else
                disp('Matrix is reducible');
            end
            
            if abs(determinate)<= tol
                disp('Matrix is singular');
            else
                disp('Matrix is invertable');
            end
            
            if is_normal_matrix(M)
                disp('Matrix is normal');
            end
            
            if is_hermitian_matrix(M)
                if isReal
                    disp('Matrix is symmetric');
                else
                    disp('Matrix is Hermitian');
                end
            end
            
            if is_anti_hermitian_matrix(M)
                if isReal
                    disp('Matrix is anti-symmetric');
                else
                    disp('Matrix is anti-Hermitian');
                end
            end
            
            if is_unitary_matrix(M)
                if isReal
                    disp('Matrix is orthognal');
                else
                    disp('Matrix is unitary');
                end
            end
            

            if is_symplectic_matrix(M)
                disp('Matrix is symplectic');
            end
            
            if isIrreducible
                fprintf('\n');

                disp('Let the matrix below enteries correspoind to an ajacency matrix');
                disp('Then the following matrix is the number of shortest paths');
                disp('from vertex i to j. That number being entry (i,j)');
                fprintf('\n');
                disp(shortest_paths(M));
            else
                fprintf('\n');
                disp('The matrix can be reduced to the following:');
                disp(reduce_matrix(M));
            end
            
            fprintf('\n');
            
            fprintf('The bounds on the spectral radius = %g \n\n',bounds_spectral_radius(M)  );
            
            fprintf('The spectral radius    = %g \n',spectral_radius(M) );
            
            fprintf('The spectral abscissa  = %g \n',spectral_abscissa(M)  );
            
            fprintf('The determinate        = %s \n',num2str(determinate ) );
            
            fprintf('\n');
            
            if Perron_Frobenius(M)
                fprintf('\nEnd of Perron - Frobenius Theorem Information')
            end
                
            fprintf('\n');
            
            fprintf('The following are the eigen-pairs of the matrix\n\n');
            
            for i=1:length(M)
                fprintf('Eigenvalue  = %s \n',num2str(eValue(i,i)) );
                fprintf('Eigenvector = \n');
                disp(eVector(:,i));
            end
            
            plot_Gershgorin_disks(M);
            plot_all_eigenvalues(M)
            plot_spectral_radius(M);
            disp('The solid blue line (line made of ".") is the circle with');
            disp('spectral radius centered at the origin');
            disp('The thin lines are the Gershgorin disks.');
            disp('The small red blocks are the eigenvalues.');
            
        else
            disp('Matrix is not square');
        end
        
        if isReal
            fprintf('\n');
            disp('Various evaluations of the norm of M using different matrix norm');
            disp('Current implementation assumes real matrices');
            fprintf('\n');
            my_matrix_norm(M,1,true);
            my_matrix_norm(M,2,true);
            my_matrix_norm(M,inf,true);
        end
    else
        disp('Parameter passed is not a matrix.');
    end
end