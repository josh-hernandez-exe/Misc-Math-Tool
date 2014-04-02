function rMatrix = reduce_matrix(M)
% Purpose:
%   Given that the passed matrix is reducible, the function finds the
%   reduced matrix by trying all possible permutation matrices.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   rMatrix = the reduced matrix of M (if possible)
%
    rMatrix = NaN(size(M)) ;

    if ~is_irreducible_matrix(M)

        n = length(M); % size or largest dimension of matrix
                       % note that irreduciability requiers
                       % matrix to be square
        
        id = 1:n; % identity permutation
                       
        pi = perms(id); % a list of permuations of the
                        % numbers from 1 to length of the
                        % matrix. will be used for permuting
                        % the rows
        
        %number of rows = number of permutations
        [numPerm,] = size(pi);
        
        I= eye(n); % idendtity matrix
                   % note that one argunment creates a square
                   % matrix        

        for i=1:numPerm
            
            currPi = pi(i,:);
            
%             % we ignore the identity permutation
%             % otherwise every matrix is reduced
%             if ~all(currPi == id)
%                 % reorders the rows of the identity 
%                 % to what the permutation function is at
%                 P= I(currPi,:);
% 
%                 tempMatrix = P * M * P';
% 
%                 if is_upper_block_triangular(tempMatrix);
%                     rMatrix = tempMatrix;
%                 end
%             end



            % reorders the rows of the identity 
            % to what the permutation function is at
            P= I(currPi,:);

            tempMatrix = P * M * P';

            if is_upper_block_triangular(tempMatrix);
                rMatrix = tempMatrix;
            end

        end
    end
end