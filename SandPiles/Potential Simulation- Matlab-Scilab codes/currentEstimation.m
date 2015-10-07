function a = currentEstimation

n = input('Enter the grid size: ');

%k = 100

%for n = k:k+300
a = zeros(n+1,n);  % Preallocate matrix
%b = zeros(n,n);
sum =0;
for i = 0:n-1
    for j = 0:n-1
        if((i == 0)&&(j == 0))
            a(i+1,j+1) = 0;
        else
            a(i+1,j+1)=(-1)^(j)*(cos(i*pi/(2*n))*sin(j*pi/n)*sin(j*pi/(2*n)))^2/(sin(i*pi/(2*n))^2 + sin(j*pi/(2*n))^2);
            %a(i+1,j+1)=(-1)^(j+1)*(cos(i*pi/(2*n)))^2*sin(j*pi/n)*sin(2*j*pi/n)/(sin(i*pi/(2*n))^2 + sin(j*pi/(2*n))^2);
            %a(i+1,j+1)=(-1)^(j+1)*(sin(j*pi/(2*n)))^2*sin(j*pi/n)*sin(2*j*pi/n)/(sin(i*pi/(2*n))^2 + sin(j*pi/(2*n))^2);
            %sum = sum + (-1)^(j+1)*(cos(i*pi/(2*n))*sin(j*pi/n)*sin(j*pi/(2*n)))^2/(sin(i*pi/(2*n))^2 + sin(j*pi/(2*n))^2);
            %sum = sum + (-1)^(i+j+1)*(sin((i+j)*pi/(2*n))*sin((i-j)*pi/(2*n))*cos(i*pi/(2*n))*cos(j*pi/(2*n)))^2/(sin(i*pi/(2*n))^2 + sin(j*pi/(2*n))^2);
            a(n+1,j+1) = a(n+1,j+1) + a(i+1,j+1);
            sum = sum + a(i+1,j+1);
        end
    end
end

a'
surf(a)
sum

% sum
% for i = 1:n
%     for j = 1:n
%         if(i == 1)
%             b(i,j) = a(i,j);
%         else
%             b(i,j) = b(i-1,j) + a(i,j);
%         end
%     end
% end
% Dec(n-k+1) = sum;
% end
% Dec