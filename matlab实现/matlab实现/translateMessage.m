function [ translated ] = translateMessage( key, message )
%输入密匙和文本，输出解密后的文本
translated = '';
charsA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
charsB = key;
    for i=1:length(message)
        symbol=upper(message(i));
        if findstr(symbol,charsA)
            symIndex = find(charsA == symbol);
            translated = [translated,lower(charsB(symIndex))];
        else
            translated = [translated,symbol];
        end
    end
end

