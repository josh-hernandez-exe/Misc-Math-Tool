function plot_Gershgorin_disks(M)
% Purpose:
%   Plots the Gershporin Disks. The program has been modified so that it
%   runs for matrices that are bigger than 4x4
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   Nothing
%

[rows,cols] = size(M);

if rows ~= cols,
    disp('Nonsquare matrix. Please input a square matrix.');
    return;
end;

[cx,cy,radius] = Gershgorin_disks(M);

xmin = min(cx-radius);
xmax = max(cx+radius);
xrange = xmax-xmin;
ymin = min(cy-radius);
ymax = max(cy+radius);
yrange = ymax-ymin;

colours = {'r','g','b','k'};

evalues = eig(M);

close all
hold on

for i=1:rows,
    [x,y] = circle_for_plot(cx(i),cy(i),radius(i));
    plot(x,y, rollOverIndex(colours,i) );
    plot(cx(i),cy(i),sprintf('%s*',rollOverIndex(colours,i)));
    if isreal(evalues(i)),
        plot(evalues(i),0,sprintf('%ss',rollOverIndex(colours,i)));
    else
        plot(real(evalues(i)),imag(evalues(i)),sprintf('%ss',rollOverIndex(colours,i)));
    end
end;

hold off

if xrange>=yrange,
    if xrange~=0
        xlim([xmin xmax]);
    end
else
    if yrange~=0
        ylim([ymin ymax]);
    end
end
axis equal

end

function thing =  rollOverIndex(array,index)
    thing =  array{   mod(index-1,length(array))+1 };
end
