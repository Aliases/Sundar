%simulates the circuit with power source-sink pair attached to requisite
%nodes

function Vh = test 

n = input('Enter the grid size: ');
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
       % b = ii           b = jj
        if ((abs(ii(1) - jj(1)) == 1)&(abs(ii(2) - jj(2)) == 0))|...
                ((abs(ii(1) - jj(1)) == 0)&(abs(ii(2) - jj(2)) == 1))
            a(i,j)= -1;
            a(i,i) = a(i,i) + 1;
        end
    end
end

%s = input('input the power source vertex in the format [x-coord y-coord]: ');
%t = input('input the power sink vertex in the format [x-coord y-coord]: ');

s = [2 1];
t = [1 2];

v = zeros(n^2,1);
ss = s(1)+ (s(2)-1)*n;
tt = t(1)+ (t(2)-1)*n;
v(ss) = 1;
v(tt) = 0;

for i = 1:n^2
    a(ss,i) = 0;
    if(i == ss)
        a(ss,ss) = 1;
    end
    a(tt,i) = 0;
    if(i == tt)
        a(tt,tt) = 1;
    end    
end

V = inv(a)*v;

Vh = zeros(n,n);

for i=1:n
    for j=1:n
        Vh(i,j) = V(i+n*(j-1));
    end    
end
 
%Vd = Vh;
Vd = zeros(n,n-1);

for i=1:n
    for j=1:n-1
        Vd(i,j) = sign(Vh(i,j) - Vh(i,j+1));
    end    
end

Vh(1,n) - Vh(1,n-1)

 %x=ones(n,1)*[1:n];
 %x=x';
 %y=ones(n,1)*[1:n];
 %surf(x,y,Vh);
  %surf(x,y,Vd);
 
 
 