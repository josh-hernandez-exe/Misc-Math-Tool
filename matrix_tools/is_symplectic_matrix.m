function isTrue = is_symplectic_matrix(M)
% Purpose:
%   Checks to see if the passed matrix is symplectic by the following
%   definition.
%
% Def :
%   omega = [   0   I_n  ;
%             -I_n   0   ]
%
% Def (Symplectic):
%   A matrix is symplectic is : M' * omega * M = omega
%   where M' is the transpose of M if it is real
%   or the conjugate transpose if N is complex
%
% Note:
%   If M is real then the definition is well recongnized, but if M is
%   complex then if M satifies this definiton then it is sometimes called
%   a congugate symplectic.
%
% Input :
%   M = Matrix of float (real or complex) values
%
% Returns :
%   isTrue = boolean value representing if the matrix is symplectic
%
    isTrue = false;

    if is_square_matrix(M)
        
        len = length(M);
        
        if mod(len,2)==0
            
            n = len/2;
            I = eye(n);
            
            omega = zeros(len);
            
            omega((n+1):len,1:n) = -I;
            omega(1:n,(n+1):len) = I;
            
            isTrue = all(all(M'*omega*M==omega));
        end
    end
end