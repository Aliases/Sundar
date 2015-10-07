function[isTopple,scoreMat,currentConfig]=topple(currentConfig,i)
    
    n=size(currentConfig,1);
    
    isTopple=zeros(n);
    scoreMat=zeros(n);    
    
    unstableSites=java.util.Stack();
    unstableSites.push(i);
	unstableSites.push(1);
    
    while unstableSites.empty==0
    
       currentSiteY=unstableSites.pop();
	   currentSiteX=unstableSites.pop();
       %disp('Found unstable site');
       %disp([currentSiteX,currentSiteY]);
       %disp('losing particles');
       isTopple(currentSiteX,currentSiteY)=1;
       
       neighbours=getNeighbours(currentSiteX,currentSiteY,n);
       
       while currentConfig(currentSiteX,currentSiteY)>= 4
           for i=1:size(neighbours,1)
              currentConfig(neighbours(i,1),neighbours(i,2))=currentConfig(neighbours(i,1),neighbours(i,2))+1;
              if currentConfig(neighbours(i,1),neighbours(i,2))==4
                unstableSites.push(neighbours(i,1));
				unstableSites.push(neighbours(i,2));
              end
              
           end
		   scoreMat(currentSiteX,currentSiteY)=scoreMat(currentSiteX,currentSiteY)+1;
		   currentConfig(currentSiteX,currentSiteY)=currentConfig(currentSiteX,currentSiteY)-4;
       end
       
    end
end