function d = test

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
        if ((abs(ii(1) - jj(1)) == 1)&(abs(ii(2) - jj(2)) == 0))|...
                ((abs(ii(1) - jj(1)) == 0)&(abs(ii(2) - jj(2)) == 1))
            a(i,j)= -1;
            a(i,i) = 4;
        end
    end
end

% c = a;
% for i = 1:n^2
%     for j = 1:n^2
%     b = a;
%     b(i,:) = [];
%     b(:,j) = [];    
%     c(i,j) = det(b);
%     end
% end
%(c(:,n^2)')*a(:,n^2)

d_11 = a;
d_1n = a;
    d_11(1,:) = [];
    d_11(:,1) = [];    
    d_1n(1,:) = [];
    d_1n(:,n^2) = [];    
 d_1ntemp = d_1n;   

 for i = 1: n^2 - 2 
    d_1n(:,i) = d_1ntemp(:,i+1);
 end
    d_1n(:, n^2 - 1) = d_1ntemp(:,1);
    dc_1n = d_1n;
    dc_1n(n^2 - 1, n^2 - 1) = 2;
    d_1nnn = d_1n;    
    d_1nnn(n^2 - 1,:) = [];
    d_1nnn(:,n^2 - 1) = [];    
 

%  d_11
%   d_1n
%  d_11 - d_1n
%   d_1nnn
%  d_1n * inv(d_11)
 inv(d_1n)* d_11
 %inv(dc_1n)* d_11
 det(d_1n)
 det(dc_1n)
 det(d_1nnn)

 
moreminor = 0 ; %1;
while moreminor == 1
    mp = input('Enter the minoring position : '); 
    b = a;
    b(mp(1),:) = [];
    b(:, mp(2)) = [];
    %a
    %b
    %eig(a)'
    %eig(b)'
    eigb = eig(b)';
    for i = 1: n^2 - 1
       eigb(i) = abs(eigb(i)); 
    end
    eig(a)'
    eigb = sort(eigb);
    moreminor = 0;
    moreminor = input('Enter 1 if you want to repeat with some other minor : ');
end


