function [ degreeSandpile]=calcDegree(n)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    degreeSandpile=4*ones(n);
    degreeSandpile(1:n,1)=3;
    degreeSandpile(1:n,n)=3;
    degreeSandpile(1,1:n)=3;
    degreeSandpile(n,1:n)=3;
    degreeSandpile(1,1)=2;
    degreeSandpile(1,n)=2;
    degreeSandpile(n,1)=2;
    degreeSandpile(n,n)=2;

end

