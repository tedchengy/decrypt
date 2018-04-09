fid = fopen('cipher.txt','r')
message=fscanf(fid, '%s')
status=fclose(fid)
charsA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
charsB = 'KQVYCSOFRZHNXWAJIDLEMPBUGT'
symbol='b'
symIndex = find(charsA=='B')
charsB(symIndex)
length(symbol)
length(message)
i=5;
upper(message(i)) == charsA
findstr(upper(message(i)),charsA)
for i=1:length(message)
    symbol=upper(message(i))
    if findstr(symbol,charsA)
        symIndex = find(charsA==upper(symbol))
        translated = char(translated,lower(charsB(symIndex)))
    else
        translated =char(translated,symbol)
    end
end

