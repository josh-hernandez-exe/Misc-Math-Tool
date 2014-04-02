function isTrue = is_irreducible_matrix(M)
% Purpose:
%   Checks to see if the matrix satifies the definition of an
%   irreducible matrix, using the theorem below. This is done by taking powers of M.
%   When a non-zero entry appears it is recorded using logical 'or'.
%   M^k represents the paths of length exactly k. So if there is a non zero
%   entry, then there is a path. Taking all power of M from 1 to n 
%   (note that the matrix must be n by n) and keeping track of non-zero
%   entries in any if the matrices. If every entry had a non-zero entry at
%   some point then the matrix is irreducible.
%
% Def (Reducible Matrix):
%   A Reducible matrix is one where there exsist permutation matrix, P
%   such that P * M * P^T is upper block triangular
%
% Def (Irreducible Matrix):
%   A Irreducible matrix is one where no such permutation matrix exsist
%   to make the given matrix upper block triangular.
%
% Theorem:
%   A matrix is irreducible if and only if the assosiated di-graph is 
%   strongly connected.
%
% Def (strongly connceted Di-Graph):
%   A di-graph is strongly connceted if there exist a path between any two
%   vertices in the graph.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = Boolean represending if the matrix is irreducible
%
    isTrue = false;
    
    if is_square_matrix(M)
        
        len = length(M);
        
        % this is a boolean array
        % every entry corresponds to if there is a path
        % of length k from vertex i to j
        % note that if every i and j has a path then
        existsPath = false(len);
        
        k=1;
        
        % M to the power of k
        % M^k represents the paths of length exactly k
        % and the entries denote the number of such paths
        % from vertex i to j in entry (i,j)
        m_to_k = M;
        
        while (k<=len) && ~all(all(existsPath))
            
            % using logical 'or' to see if there are
            % non-zero entries in m_to_k . This
            % corresponds to exsisting paths.
            existsPath = existsPath | abs(m_to_k);
            
            m_to_k = m_to_k * M;
            
            k=k+1;
        end
        
        isTrue = all(all(existsPath)) ;
    end
end