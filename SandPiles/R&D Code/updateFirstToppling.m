function [ firstToppling_i]=updateFirstToppling(firstToppling_i,isTopple_i,t)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
    isTopple_i=t*isTopple_i;
	n=size(isTopple_i,1);
	for i=1:n
		for j=1:n
			if isTopple_i(i,j)~=0
				firstToppling_i(i,j)=min(firstToppling_i(i,j),isTopple_i(i,j));
			
			end
	end
    

end

