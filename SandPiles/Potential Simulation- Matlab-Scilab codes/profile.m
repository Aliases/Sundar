function sum = profile(nmin)

%profile = zeros(n);
l = 100;

%sum = zeros(nmin+l);
for n = nmin : nmin + l    
    %sum = 0;
    for i = 1 : n
        for j = 1 : n
            if((i == 1) &(j == 1))
                %sum = 0;
                sum(n - nmin +1) = 0;
            else
                %profile(i,j) = (cos((i-1)*pi/(2*n))*sin((j-1)*pi/(2*n))*sin((j-1)*pi/n))^2/((sin((j-1)*pi/(2*n)))^2 + (sin((i-1)*pi/(2*n)))^2) ; %for latest adjacent corners
                %profile(i,j) = (sin((j-i)*pi/(2*n))*sin((j+i-2)*pi/(2*n))*cos((i-1)*pi/(2*n))*cos((j-1)*pi/(2*n)))^2/((sin((j-1)*pi/(2*n)))^2 + (sin((i-1)*pi/(2*n)))^2) ; %for opposite corners
                sum(n - nmin +1) = sum(n - nmin +1) + (sin((j-i)*pi/(2*n))*sin((j+i-2)*pi/(2*n))*cos((i-1)*pi/(2*n))*cos((j-1)*pi/(2*n)))^2/((sin((j-1)*pi/(2*n)))^2 + (sin((i-1)*pi/(2*n)))^2) ; %for opposite corners
                %sum = sum + (sin((j-i)*pi/(2*n))*sin((j+i-2)*pi/(2*n))*cos((i-1)*pi/(2*n))*cos((j-1)*pi/(2*n)))^2/((sin((j-1)*pi/(2*n)))^2 + (sin((i-1)*pi/(2*n)))^2) ; %for opposite corners
            end
        end
    end
end

%Sum matches the formula for N(a,b) on page 5. 
%In code, no (-1)^power factor
%It seems that all elements of sum array will have same value 