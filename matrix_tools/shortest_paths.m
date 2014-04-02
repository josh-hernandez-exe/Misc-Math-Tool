function paths = shortest_paths(M)
% Purpose:
%   If the passed matrix is interperted as an adjacency matrix then this
%   function will construct a new matrix where entry (i,j) is the number of
%   shortest paths from vertex i to j.
%
%   This is done by taking powers of M. When a non-zero entry appears it is
%   recorded. This is since any higher power of M results in a longer path.
%
% Note:
%   is_irreducible_matrix is not used as it would be inefficent. Instead it
%   is calculated with the calculation of path. Since the algorithms for
%   each are very similar, intergrating the two is simple. If it is
%   determined that M is reducible, then the matrix is filled with zeros
%   before being returned
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   paths = matrix of shortest paths from vertex i to j found at
%             entry (i,j)
%
    paths = zeros(size(M));
    
    isIrreducibleMatrix = false;
    
    % i dont use is_irreducible_matrix as it would be inefficent
    % as the algorithms are very similar
    if is_square_matrix(M)
        
        len = max(size(M));
        
        % this is a boolean array
        % every entry corresponds to if there is a path
        % of length k from vertex i to j
        % note that if every i and j has a path then
        
        existsPath = false(len);
        
        k=1;
        
        m_to_k = M;
        
        while (k<=len) && ~all(all(existsPath))
            
            existsPath = existsPath | abs(m_to_k);
            
            % the new paths discovered are non-zero entires
            % in the currenct M^k but not the entires that where
            % non-zero in the last iteration
            % a logical vector of new paths
            newPaths =  existsPath & (~paths)  ;
            
            paths(newPaths) = m_to_k(newPaths);
            
            m_to_k = m_to_k * M;
            
            k=k+1;
        end
        
        isIrreducibleMatrix = all(all(existsPath)) ;
    end

    if ~isIrreducibleMatrix
        paths = 0*paths;
    end

end