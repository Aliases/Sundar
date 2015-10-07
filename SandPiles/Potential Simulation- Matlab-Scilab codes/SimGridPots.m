function VinvMat = SimGridPots()
n = input('Enter the grid size: ');

% l = 30;
% u = 50;
%for n = l:u
    
a = zeros(n^2,n^2);  % Preallocate matrix

for i = 1:n^2
    for j = 1:n^2
        %i1 = i
        ii = [mod(i,n) 1+(i - mod(i,n))/n];
        if (ii(1) == 0)
           ii(1) = n;
           ii(2) = ii(2) - 1;
        end
        jj = [mod(j,n) 1+(j - mod(j,n))/n];
        if (jj(1) == 0)
           jj(1) = n;
           jj(2) = jj(2) - 1;
        end
        if ((abs(ii(1) - jj(1)) == 1)&(abs(ii(2) - jj(2)) == 0))|...
                ((abs(ii(1) - jj(1)) == 0)&(abs(ii(2) - jj(2)) == 1))
            a(i,j)= -1;
            a(i,i) = 4;
        end
    end
end

v = zeros(n^2,1);
%s = input('input the impulse vertex in the format [x-coord y-coord]: ');
centX = ceil(n/2);
centY = ceil(n/2);

s = [centX centY];
ss = s(1)+ (s(2)-1)*n;
v(ss) = 1;

for i = 1:n^2
    a(ss,i) = 0;
    if(i == ss)
        a(ss,ss) = 1;
    end
end

V = inv(a)*v;


for i=1:n^2
        Vinv(i) = V(i);
end

%VMat = reshape(V, n,n);
VinvMat = reshape(Vinv, n,n);
surf(VinvMat);


%pat(n) = VinvMat(n,n);

%end

% Vinv = Vinv';
% SqrVinv = reshape(Vinv, n,n)

%Here we will estimate the coefficients of a polynomial we will be fitting
%to the observed data stored in Vinv. Vinv stores the inverses of the
%green's function response to a unit potential applied at a particular
%vertex. 

%The matrix B stores values of dfferent basis elements at the respective
%points of grid. The current basis set is 1, x, y, x^2, y^2, xy, x^3, y^3,
%x^2y, xy^2, x^4, y^4, x^3y, xy^3, x^2y^2 : basically 4 degree polynomial in x and y
% 
% for y = 1:n
%     for x = 1:n        
% for fitting potential values        
%         DeFac = 10^((x*y)/(x+y)^4);    
%         B(x+n*(y-1),1)=      1 * DeFac ;
%         B(x+n*(y-1),2)=    x^-1 * DeFac ;
%         B(x+n*(y-1),3)=    y^-1 * DeFac ;
%         B(x+n*(y-1),4)=    x^-2 * DeFac ;
%         B(x+n*(y-1),5)=    y^-2 * DeFac ;
%         B(x+n*(y-1),6)=    (x*y)^-1 * DeFac ;
%         B(x+n*(y-1),7)=    x^-3 * DeFac ;
%         B(x+n*(y-1),8)=    y^-3 * DeFac ;
%         B(x+n*(y-1),9)=    x^-4 * DeFac ;
%         B(x+n*(y-1),10)=   y^-4 * DeFac ;
%         B(x+n*(y-1),11)=  (y^-1)*(x^-3)* DeFac ;
% %       B(x+n*(y-1),12)=  (x^-1)*(y^-3) * DeFac ;
% %       B(x+n*(y-1),13)=  (y^-1)*(x^-2) * DeFac ;
% %       B(x+n*(y-1),14)=  (x^-1)*(y^-2) * DeFac ;
% %       B(x+n*(y-1),13)=  (x^2)*(y^2)* DeFac ;

% for fitting inverses of potential values     
%         DeFac = 1 ;%10^(((n-x+1)*(n-y+1))/(2*n-x-y+1)^2.5);
%         B(x+n*(y-1),1)=    1 * DeFac;
%         B(x+n*(y-1),2)=    x * DeFac;
%         B(x+n*(y-1),3)=    y * DeFac;
%         B(x+n*(y-1),4)=    x^2 * DeFac;
%         B(x+n*(y-1),5)=    y^2 * DeFac;
%         B(x+n*(y-1),6)=    (x*y)* DeFac;
%         B(x+n*(y-1),7)=    x^3 * DeFac;
%         B(x+n*(y-1),8)=    y^3 * DeFac;
%         B(x+n*(y-1),9)=    x^4 * DeFac;
%         B(x+n*(y-1),10)=   y^4 * DeFac;
%         B(x+n*(y-1),11)=   y*(x^3)* DeFac;
%         B(x+n*(y-1),12)=   x*(y^3)* DeFac;
% %     B(x+n*(y-1),13)=  (y^1)*(x^2) *10^((x*y)/(x+y)^4);
% %     B(x+n*(y-1),14)=  (x^1)*(y^2) *10^((x*y)/(x+y)^4);
% %     B(x+n*(y-1),13)=  (x^2)*(y^2)*10^((x*y)/(x+y)^4);
%     end
% end

%Now let the vector C store the coeffecients of polynomial approximation to
%Vinv. Then BC = Vinv (approximately), using moore-Penrose pseudo inverses
%we have, C = inv(B'*B) * B' * Vinv which inturn implies that the error vector is
%Vinv - BC, or B * inv(B'*B) * B' * Vinv - Vinv

%C = inv(B'*B) * B' * Vinv;
%Error = V - B*inv(B'*B) * B' * V;
%ErrorInv = Vinv - B*inv(B'*B) * B' * Vinv;

% The normalised error ir just each deviation divided by the actual value

%for i = 1:n^2
 %  NorErr(i) = Error(i)/V(i);
 %   NorErrInv(i) = ErrorInv(i)/Vinv(i);
%end

%SqrNorErr =  reshape( NorErr,n,n);
%SqrNorErrInv = reshape( NorErrInv,n,n);
%out = SqrNorErrInv;

 
 
 
 %Now we try to fit only the central region of the grid, say excluding the
%c point wide band on each side

% c = ceil(log2(n));
% SqrVinvCent = SqrVinv(c:n-c , c:n-c);
% VinvCent = reshape(SqrVinvCent, (n- 2*c + 1)^2 , 1);
% 
% 
% for y = 1:(n - 2*c + 1)
%     for x = 1:(n - 2*c + 1)
        
% for fitting inverses of potential values     
%         DeFact = 1 ;%10^(((n-x+1)*(n-y+1))/(2*n-x-y+1)^2.5);
%         Bt(x+(n - 2*c + 1)*(y-1),1)=    1 * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),2)=    (x+c) * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),3)=    (y+c) * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),4)=    (x+c)^2 * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),5)=    (y+c)^2 * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),6)=    ((x+c)*(y+c))* DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),7)=    (x+c)^3 * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),8)=    (y+c)^3 * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),9)=    (x+c)^4 * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),10)=   (y+c)^4 * DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),11)=   (y+c)*((x+c)^3)* DeFact;
%         Bt(x+(n - 2*c + 1)*(y-1),12)=   (x+c)*((y+c)^3)* DeFact;
% %     Bt(x+(n - 2*c + 1)*(y-1),13)=  ((y+c)^1)*((x+c)^2) *  DeFact;
% %     Bt(x+(n - 2*c + 1)*(y-1),14)=  ((x+c)^1)*((y+c)^2) * DeFact;
% %     Bt(x+(n - 2*c + 1)*(y-1),13)=  ((x+c)^2)*((y+c)^2)*  DeFact;
%     end
% end
% 
% Ct = inv(Bt'*Bt) * Bt' * VinvCent;
% ErrorInvCent = VinvCent - Bt*Ct;
% 
% for i = 1:(n- 2*c + 1)^2
%     NorErrInvCent(i) = ErrorInvCent(i)/VinvCent(i);
% end
% 
% SqrNorErrInvCent = reshape( NorErrInvCent, n - 2*c + 1 , n - 2*c + 1 );
% out = SqrNorErrInvCent;
