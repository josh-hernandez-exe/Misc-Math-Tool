function isTrue = is_matrix(M)
% Purpose:
%   Checks to see if the passed parameter is a matrix. This is done by
%   looking at the size vector of M. if the size vector is 1x2, then it
%   is a two dimensional array, which we interpert to be a matrix.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean representing if the parameter is a matrix
%

    % len is an array of the lengths for each dimension
    % of M
    len = size(M);
    
    % max(size(len)) is the number of dimensions M has
    isTrue =  max(size(len))==2;
end