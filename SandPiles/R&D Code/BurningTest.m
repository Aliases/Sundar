function [isTrue]=BurningTest(currentConfig_i,n)
isTrue=0;
burnt=zeros(n);
numBurnt=0;
flag=1;
while(flag==1)
    flag=0;
    %disp(burnt);
    for u=1:n
        for v=1:n
           if burnt(u,v)==0 
                neighbours=getNeighbours(u,v,n);
                unburntNeighbours=0;
                %fprintf('Checking for burning\n')
                %disp([u,v]);
                
                %disp(neighbours);
                for i=1:size(neighbours,1)
                    %disp(burnt(neighbours(i)));
                    if burnt(neighbours(i,1),neighbours(i,2))==0
                        unburntNeighbours=unburntNeighbours+1;
                    end
                 
                end
                
                if currentConfig_i(u,v)>=unburntNeighbours
                    burnt(u,v)=1;
                    flag=1;
                    numBurnt=numBurnt+1;
                    
                    %disp(unburntNeighbours);
                    %disp('Burnt');
                end
                
                
           end
        end
    end
end

if numBurnt==n*n
    isTrue=1;
end

end