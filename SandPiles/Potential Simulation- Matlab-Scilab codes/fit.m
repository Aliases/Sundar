function sam = input(n)

% used for creating sample potential drop surfaces for matching with
% observation

for x = 1:n
    for y = 1:n
        sam(x,y) = 10^(((n-x+1)*(n-y+1))/(2*n-x-y+1)^2.5);
    end
end

surfc(sam);