function isTrue = is_upper_triagular_matrix(M)
% Purpose:
%   Checks to see if the passed matrix is upper triangular by the
%   definition below
%
% Def:
%   A matrix is upper triangular if M(i,j)=0 for all i>j
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean representing if the matrix is uppwe triangular
%
    isTrue = false;

    if is_matrix(M)
        
        [rowSize,colSize] = size(M);

        isTrue = true;

        i=2;
        j=1;

        while (i<=rowSize) && (j<=colSize) && isTrue
            
            % test every col below the main diagonal
            % to see if they are all zeros
            isTrue = isTrue && ~any( M(i:rowSize,j) );
            
            i=i+1;
            j=j+1;
        end
    end
end