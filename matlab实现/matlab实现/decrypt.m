clear all
fid = fopen('cipher.txt','r')
message=fscanf(fid, '%s')
status=fclose(fid)
tabulate(message')
%frequency=length(find(message=='a'))
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
myKey = 'KQVYCSOFRZHNXWAJIDLEMPBUGT' %³õÊ¼ÃÜ³×
        %KXVMCNOPHQRSZYIJADLEGWBUFT   %rightÃÜ³×
myKey3 = LETTERS
while ~strcmp(myKey,myKey3)
    myKey3=myKey
    i=0;
    j=25;
    m=1;
    while j>0
        i=0;
        while i<j
            myKey1=[myKey(1:i),myKey(i+m+1),myKey(i+2:i+m),myKey(i+1),myKey(i+m+2:26)]
            score1 = score(translateMessage(myKey, message));
            score2 = score(translateMessage(myKey1, message))
            if score2 > score1
                myKey=myKey1
            end
            i=i+1;
        end
        m=m+1;
        j=j-1;
    end
end

myKey
translated=translateMessage(myKey, message)
score (translated)

