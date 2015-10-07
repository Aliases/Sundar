function sum = test

%ns = input('Enter the starting value : ');
%ne = input('Enter the ending value : ');
n = input('Enter the starting value of n  : ');

%n = 1000;
%sum = 0;

%K = .01;
%fit = zeros(n);
l = 100;
% j = n;

for j = n : n + l
    sum(j + 1 - n) = 0;
%    K = pi/j;
    k = 1;
    for i = 1: j
        %fit(i) = (sin(i*pi/j)*sin(i*pi/(2*j)))^2 ;
        a = (pi/(2*j))*(cos(i*pi/(2*j)))^2/((sin(k*pi/(2*j)))^2 + (sin(i*pi/(2*j)))^2) ;                
        %fit(i) = (pi/(2*n))*(cos(i*pi/(2*n)))^2/(K^2 + (sin(i*pi/(2*n)))^2) ;
        %fit(i) = K^(2)*(1-K^2)*(pi/(2*n))*(cos(i*pi/(2*n)))^2/(K^2 + (sin(i*pi/(2*n)))^2) ;
        sum(j + 1 - n) = sum(j + 1 - n) + a; % fit(i);        
    end
    sum(j + 1 - n) = (((((sin(k*pi/(2*j)))^(-2) + 1)^(.5) - 1)*pi/2 + pi/(4*j*(sin(k*pi/(2*j)))^2)) - sum(j + 1 - n));
end

%intVal =  K^(2)*(1-K^2)*((1 + 1/K^2)^(1/2)*atan((1 + 1/K^2)^(1/2)*tan((n-1)*pi/(2*n))) - (n-1)*pi/(2*n) - ( (1 + 1/K^2)^(1/2)*atan((1 + 1/K^2)^(1/2)*tan(pi/(2*n))) - pi/(2*n))) ;

%intVal
%sum