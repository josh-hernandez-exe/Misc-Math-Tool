function sample_worksheet()
% Purpose:
%   The aim of this assignment is to start developing a MatLab/Octave 
%   toolkit for dealing with matrix problems. This worksheet will test that
%   toolkit with various matrices.
%
% Input :
%   Nothing
%
% Returns :
%   Nothing
%
    test1 = [0,1,0,0,0,0;
             0,0,1/4,1/4,1/4,1/4;
             1/6,1/6,1/6,1/6,1/6,1/6;
             0,0,0,0,1/2,1/2;
             0,0,0,1/2,0,1/2;
             1/6,1/6,1/6,1/6,1/6,1/6;];
         
         
	test2 = [0,0,5;
             0.5,0,0;
             0,0.5,0];
    n=5;
    r=10;
         
    test3 = r*(rand(n)-0.5);
    test4 = r*(rand(n)-0.5);
         
         
    %these matrices are found on pg. 172 of Keyfitz and Caswell
    A1 = [0.03063,0.6094,0.0913;0.9924,0,0;0,0.9826,0];
    A2 = [0,0.8784,0.1316;0.9924,0,0;0,0.9826,0];
    A3 = [0,0.0641,0.9603;0.9924,0,0;0,0.9826,0];
    
    %some markov chain
    mc1 = [.2,.4,.1,.1,.2;.3,.2,.1,.3,.1;.4,.1,.1,.3,.1;0,0,0,.6,.4;0,0,0,.3,.7];

    theta = rand(1)*2*pi;
    
    rot = [ cos(theta),-sin(theta);sin(theta),cos(theta)];
    
    %random complex
    
    %random radius and angle
    zRand1 = r*rand(n).*exp(rand(n)*2*pi*1i);
    
    %random real and complex parts
    zRand2 = r*rand(n)+r*1i*rand(n);
    
    testMatrix(test1);
    testMatrix(test2);
    testMatrix(test3);
    testMatrix(test4);
    testMatrix(A1);
    testMatrix(A2);
    testMatrix(A3);
    testMatrix(mc1);
    testMatrix(rot);
    testMatrix(zRand1);
    testMatrix(zRand2);
end

function testMatrix(M)
% Purpose:
%   Runs properties_matrix on the passed matrix then waits for user input
%   before ending.
%
% Input :            
%   M = Matrix of float (real or complex) values
%
% Returns :
%   Nothing
%
    properties_matrix(M);
    fprintf('\n');
    disp('Push any key to continue');
    pause;
end