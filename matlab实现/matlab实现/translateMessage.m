function [ translated ] = translateMessage( key, message )
%�����ܳ׺��ı���������ܺ���ı�
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

