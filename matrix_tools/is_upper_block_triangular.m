function isTrue = is_upper_block_triangular(M)
% Purpose:
%   Checks to see if the passed matrix is upper block triangular.
%   This is done by checking the following conditions
%     - an upper left square block (if square)
%     - a lower right square block (enforced by algorithm)
%     - a lower left retagular zero block (enforced/checked)
% 
%	This is done by checking the lower left rectangular block
%	to see if it composed of zeros.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean representing if the matrix is upper block triangular
%
    isTrue = false;

    if is_matrix(M)
        [rowSize,colSize] = size(M);

        i=rowSize;
        j=colSize-1;

        while (i>1) && (j>1) && ~isTrue
            
            % 'any' returns true if there is at least
            % one non-zero element in a vector
            isTrue = isTrue || ~any(any(   M(i:rowSize,1:j )    ));
            
            i=i-1;
            j=j-1;
        end
    end
end