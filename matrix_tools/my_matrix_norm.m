function norm = my_matrix_norm(A, p,varargin)
% Purpose:
%   Attempts to evaluate the matrix norm of A induced by the vector-p-norm.
%   This is done with a maxamization of A*x where |x|=1
%
% Definition:
%   |A|_p = max( |A*x|_p such that |x|=1 )
%
% Input :
%   A           = Matrix of float (real or complex) values
%   p           = index of which vector norm to use
%   varargin{1} = boolean flag for test functions
%   varargin{2} = boolean flag for debug functions and options
%
% Returns :
%   norm = the aproximate value of the norm of A

    if (max(size(varargin))>=1)
       test =  varargin{1};
    else
       test = false;
    end
    
    if (max(size(varargin))==2)
        debug =  varargin{2};
    else
        debug = false;
    end    
    
    [row,col] = size(A);

    if (row<2 && col<2)
        error('my_matrix_norm was not given a matrix');
    end


    %we want to maximize normNorm
    f = @(x) -normNorm(A,x,p);

    x0 = ones(col,1);
    
    options = optimset('MaxFunEvals',999999,'MaxIter',9999);

    [x,norm] = fminsearch(f,x0,options);

    norm = -norm;
    
    if(test)
        test_my_matrix_norm(A,p,norm)
    end
    
    if(debug)
        disp('x_min = ');
        disp(x); 
    end
    
end

function norm = normNorm(A,x,p)
%normalized vector norm

    if( any(x) && (1/my_norm(x,p))~=inf )
        
        norm = my_norm(A*x,p)/ my_norm(x,p);
    else
        %divison by norm is too large
        %or vector is zero
        error('normNorm in my_matrix_norm was given zero vector');
    end
end

function test_my_matrix_norm(A,p,norm)

    if(p==1 )
        %max col sum
        normtest = max(sum(abs(A)));
    elseif(p==2 )
        %spectral norm
        %eigenvalues of A'A are all real
        eigenVals = eig( A'*A ) ;

        normtest = max(eigenVals);
        normtest = sqrt(normtest);
        
    elseif(p==inf )
        %max row sum
        normtest = max(sum(abs(A')));
    end
    
    
    fprintf('Naive  p = %4d - norm = %f\n',p,norm);
    if(p==1 || p==2 || p==inf)
        fprintf('Actual p = %4d - norm = %f\n',p,normtest);
    end
end