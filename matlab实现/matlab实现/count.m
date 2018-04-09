function [c] =count( message ,string)
%二元组计数
c = size(strfind(message,string),2);
end

