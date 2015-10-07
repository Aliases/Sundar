function [neighbours]=getNeighbours(currentSiteX,currentSiteY,n)
    neighbours=[];
	currentSite=[currentSiteX currentSiteY];
    if currentSite(1)>1
       neighbours=[neighbours; [currentSite(1)-1,currentSite(2)]];
    end
    
    if currentSite(1)<n
       neighbours=[neighbours; [currentSite(1)+1,currentSite(2)]];
    end
    
    
    if currentSite(2)>1
       neighbours=[neighbours; [currentSite(1),currentSite(2)-1]];
    end
    
    if currentSite(2)<n
       neighbours=[neighbours; [currentSite(1),currentSite(2)+1]];
    end
    
end