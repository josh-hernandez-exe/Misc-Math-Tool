function norm = my_norm(v, p)
% Purpose:
%   Attempts to evaluate the vector-p-norm of v
%
% Definition:
%   |v|_p = ( sum( v^p )  )^(1/p)
%
% Input :
%   v = vector to which we take the norm of
%   p = which power to use in the norm
%
% Returns :
%   norm = the value of the p-norm of v

    if(p>=0 && p<inf)
        norm = sum( abs(v).^p );
    
        norm = norm.^(1/p);
    elseif(p==inf)
        norm = max(abs(v));
    else
        error('Invalid p was given to my_norm');
    end
end

