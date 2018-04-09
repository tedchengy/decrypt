clear
clc
ar='abcdefghijklmnopqrst'
q = size(strfind(ar,'ac'),2)
fid = fopen('cipher.txt','r')
title=fscanf(fid, '%s')
message=title
status=fclose(fid);
charsA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
charsB = 'KQVYCSOFRZHNXWAJIDLEMPBUGT'
myKey='KQVYCSOFRZHNXWAJIDLEMPBUGT'
i=1
m=1
myKey(1:26)
%myKey1=[myKey(1:i),myKey(i+m),myKey(i+1:i+m),myKey(i),myKey(i+m+1:26)]
a1=[myKey(1:0),myKey(2),myKey(1),myKey(3:26)]
a2=[myKey(1:1),myKey(3),myKey(2),myKey(4:26)]
a3=[myKey(1:2),myKey(4),myKey(3),myKey(5:26)]
a25=[myKey(1:24),myKey(26),myKey(25),myKey(27:26)]

myKey3=myKey
i=0
j=25
m=1
t=translateMessage(myKey, message)
s='abc'
t='cba'
c=char(s,t)