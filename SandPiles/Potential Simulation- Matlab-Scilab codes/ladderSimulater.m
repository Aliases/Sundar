function v = test 

m = input('Enter the ladder size range : ');
l = 3;
for n = l:m    
    a = -2*eye(2*n+2,2*n+2);  % Preallocate matrix
    for i = 2:2*n+1
        for j = 1:2*n+2        
            if (abs(i - j) == 1)            
                if (i < n+1)
                a(i,j)= min(i,j);     
                end
                if (i == n+1)
                a(i,j)= n;
                end               
                if (i > n+1)
                a(i,j)= 2*n + 1 - min(i,j);
                end
                a(i,i) = a(i,i) - a(i,j);
            end       
        end
        a(i,2*n+2) = 2;
        b(i) = 0;
    end
    a(1,1) = 1;
    a(2*n+2,2*n+2) = 1;
    b(1) = 1;
    b(2*n+2) = 0;
    c = inv(a)*b';
    v(n-l+1) = 1/c(2*n + 1);
end
