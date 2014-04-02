function [cx,cy,radius] = Gershgorin_disks(M)
% Purpose:
%   Calculates the center and the radius of gershgorin disks in
%   the complex plain.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   cx      = x-coordinate of the center
%   cy      = y-coordinate of the center
%   radius  = the radius of the disk 
%

[rows,cols] = size(M);

if rows ~= cols,
    disp('Nonsquare matrix. Please input a square matrix.');
    return;
end;

cx = zeros(rows,1);
cy = zeros(rows,1);
radius = zeros(rows,1);

for i=1:rows,
    if isreal(M(i,i)),
        cx(i) = M(i,i);
        cy(i) = 0;
    else
        cx(i) = real(M(i,i));
        cy(i) = imag(M(i,i));
    end
    currentRow = M(i,:);
    currentRow(i) = 0;
    radius(i) = sum(abs(currentRow));
end;