function [ firstToppling_i,scoreMat_i,firstToppling_j,scoreMat_j,scoreMat_diff ] = SandpileSim( n,i,j )
%UNTITLED Summary of this function goes here
% i>j
%   Detailed explanation goes here
currentConfig_i=zeros(n);
currentConfig_j=zeros(n);

scoreMat_i=zeros(n);
scoreMat_j=zeros(n);

%degreeSandpile=calcDegree(n);
degree=4;

firstToppling_i=inf*ones(n);
firstToppling_j=inf*ones(n);

% if i==1
    % degree_i=2;
% else
    % degree_i=3;
% end

% if j==1
    % degree_j=2;
% else
    % degree_j=3;    
% end

t=0;

while BurningTest(currentConfig_i,n)==0 || BurningTest(currentConfig_j,n)==0
    currentConfig_i(i,1)=currentConfig_i(i,1)+1;
    currentConfig_j(j,1)=currentConfig_j(j,1)+1;
%     if BurningTest(currentConfig_i,n)==1
%        disp(t);
%        %disp(currentConfig_i');
%        fprintf('i reached recurrent config first'); 
%        pause(1);
%     end
%     if BurningTest(currentConfig_j,n)==1
%         disp(t);
% %        disp(currentConfig_j');
%        fprintf('j reached recurrent config first'); 
%        pause(1);
%     end
	t=t+1;
    if currentConfig_i(i,1)>=degree
       %disp('Simulating avalanche in i');
       [isTopple_i,scoreMat_temp,currentConfig_i]=topple(currentConfig_i,i);
	   %disp(isTopple_i);
	   %pause(0.5);
       scoreMat_i=scoreMat_temp+scoreMat_i;
       firstToppling_i=updateFirstToppling(firstToppling_i,isTopple_i,t);
    end
    if currentConfig_j(j,1)>=degree
       %disp('Simulating avalanche in j');
       [isTopple_j,scoreMat_temp,currentConfig_j]=topple(currentConfig_j,j); 
	   %disp(isTopple_j);
	   %pause(0.5);
       scoreMat_j=scoreMat_temp+scoreMat_j;
       firstToppling_j=updateFirstToppling(firstToppling_j,isTopple_j,t);
    end
    
    disp(t);
    %disp(firstToppling_i);
    %disp(firstToppling_j);
%     disp(currentConfig_i');
%     disp(currentConfig_j');

    %pause(1);
end
fprintf('The recurrent configs are\n');
disp(currentConfig_i');
disp(currentConfig_j');
scoreMat_diff=scoreMat_j-scoreMat_i;
disp(scoreMat_i);
disp(scoreMat_j);
disp(scoreMat_diff');
disp(firstToppling_i');
disp(firstToppling_j');


end

