function isTrue = is_primitive_matrix(M) 
% Purpose:
%   Checks to see if the passed matrix is primitive by the following
%   definition.
%
% Definition:
%     A nonnegative square matrix A=(aij) is said to be a primitive matrix
%     if there exists k such that A^k is a positive matrix.
%
% Note:
%   This function assume that def1 in the function is_positive_matrix is
%   being used.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = a boolean representing if the matrix is primitive
%

    isTrue = false;
    
    if is_square_matrix(M) && is_nonnegative_matrix(M)
        
        len = max(size(M));
        
        k=1;
        % M to the power of k
        m_to_k = M;
 
        while (k<=len) && ~isTrue
            
            m_to_k = m_to_k * M;
            
            if is_positive_matrix(m_to_k)
                isTrue = true;
            end
            
            k=k+1;
        end
    end
end

