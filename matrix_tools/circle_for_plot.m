function [x,y] = circle_for_plot(x0,y0,radius)
% circle_for_plot(x0,y0,radius)
%
% Returns [x,y] coordinates for a circle centred at (x0,y0) and with radius
% radius.
t = 0:0.01:2*pi;
x = x0+radius*cos(t);
y = y0+radius*sin(t);