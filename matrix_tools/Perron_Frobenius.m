function canApply = Perron_Frobenius(M)
% Purpose:
%   Checks to see if the Perron Frobenius theorem can be applied to the
%   passed matrix. If it is able to, then it will display the information
%   given by the theorem. It will also base the output based off the
%   specific case that the matrix calls into.
%
% Statment of Theorem ( 7.2.1.4 Keyfitz and Caswell ):
% 
% The Perron?Frobenius theorem describes the eigenvalues and eigenvectors of 
% a nonnegative matrix A. Its most important conclusion is that there generally 
% exists one eigenvalue that is greater than or equal to any of the others in magnitude. 
% Without loss of generality, we will call this eigenvalue ?1; it is called the 
% dominant eigenvalue of A.
% 
%     Primitive matrices: If A is primitive, then there exists a real, positive
%     eigenvalue ?1 that is a simple root of the characteristic equation. This 
%     eigenvalue is strictly greater in magnitude than any other eigenvalue. 
%     The right and left eigenvectors w1 and v1 corresponding to ?1 are real and
%     strictly positive. There may be other real eigenvalues besides ?1, but ?1 
%     is the only eigenvalue with nonnegative eigenvectors.
% 
%     Irreducible but imprimitive matrices: 
%     If the matrix A is irreducible but  imprimitive, with index of
%     imprimitivity d, then there exists a real positive  eigenvalue ?1
%     which is a simple root of the characteristic equation. The associated
%     right and left eigenvectors w1 and v1 are positive. The dominant eigenvalue
%     ?1 is greater than or equal in magnitude to any of the other eigenvalues; i.e.,
%     ?1 ? |?i| i > 1
%     but the spectrum of A contains d eigenvalues equal in magnitude to
%     ?1. One is ?1 itself; the others are the d ? 1 complex eigenvalues
%
%     Reducible matrices: 
%     If A is reducible, there exists a real eigenvalue ?1 ? 0 with corresponding 
%     right and left eigenvectors w1 ? 0 and v1 ? 0. 
%     This eigenvalue ?1 ? |?i| for i > 1.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   canApply = boolean variable that represents if the Perron Frobenius
%               theorem can be applied.
%   
    canApply = true;

    if is_square_matrix(M)
             
        [eVector,eValue] = eig(M);
        
        % Note that :
        %   lambdaMax = largest eigenvalue (dominate eigenvalue)
        %   vMax      = eigen coloumn vector(s) corespoding to lambdaMax
        %                   there could be more that one
        
        lambdaMax = max(diag(eValue)); 

        % logical indexing is used
        vMax = eVector(:, diag(eValue)==lambdaMax  );
        
        if is_nonnegative_matrix(M)
            
            % basic info
            fprintf('\n');
            disp('The Perron - Frobenius Theorem ');
            fprintf('\n');
            disp('Let lambda_1 = largest eigenvalue (dominate eigenvalue)');
            disp('Let   v_1    = eigen coloumn vector(s) corespoding to lambda_1');
            disp('Let   w_1    = eigen   row   vector(s) corespoding to lambda_1');
            fprintf('\n\n');
            fprintf('lambda_1 =');
            disp(lambdaMax);
            fprintf('v_1 = \n');
            disp(vMax);
            fprintf('\n');

            if is_irreducible_matrix(M)
                
                % information that the theorem provides that gained from
                % knowing that the matrix is irreducible
                fprintf('lambda_1 > 0 \n');
                fprintf('w_1 > 0 \n');
                fprintf('v_1 > 0 \n');
                fprintf('\n');
                
                if is_primitive_matrix(M)

                    fprintf('There exsits a positive integer "d" such that:\n\n');
                    fprintf('lambda_1 = | lambda_j  |       for all  such that 2<=j<=d\n');
                    fprintf('lambda_1 > | lambda_j  |       for all  j>d \n');
                else
                    fprintf('lambda_1 > | lambda_j  |       for all  j>1 \n');
                end
            else
                fprintf('lambda_1 >= 0 \n');
                fprintf('w_1 >= 0 \n');
                fprintf('v_1 >= 0 \n');
                fprintf('lambda_1 >= | lambda_j  |       for all  j>1 \n');
            end
        else
            disp('Cannot apply Perron Frobenius theorem');
            canApply = false;
        end
    else
        canApply = false;
        disp('Not given a square matrix, thus cannot apply Perron Frobenius theorem');
    end
end