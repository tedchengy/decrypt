function [c] =count( message ,string)
%��Ԫ�����
c = size(strfind(message,string),2);
end

