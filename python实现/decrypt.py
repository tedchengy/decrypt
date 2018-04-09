# -*- coding: utf-8 -*-
from collections import Counter
import re
import sys, random

#environment：python 2.7

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = open("ciphertext.txt").read().lower()
    
    englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
    ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    dict_text = dict(Counter(myMessage))
    print dict_text
    print "###################################################################"
    dict_reverse= sorted(dict_text.iteritems(), key=lambda d:d[1],reverse=True)
    str_text=str(dict_reverse)
    print str_text
    print "###################################################################"
    list_text=([word.lower() for word in str_text if word.isalpha()])
    set_text = sorted(set(list_text),key=list_text.index)
    setup_text=[s.upper() for s in set_text]
    print setup_text
    print "###################################################################"
    myKey=LETTERS
    j=0
    while(j<26):
        i=0
        while(myKey[j] != setup_text[i]):
            i=i+1
        myKey=myKey[0:j]+ETAOIN[i]+myKey[j+1:26]
        j=j+1
    print("first key: %s" % (myKey))
    print "###################################################################"
    
           # ABCDEFGHIJKLMNOPQRSTUVWXYZ
#    myKey = 'KQVYCSOFRZHNXWAJIDLEMPBUGT'  #test
#    myKey = 'KQVYCNOLHZRSXMIJADWEGPBFUT' #convergence false 
#    myKey = 'KQVMCNOPHZRSXYIJADLEGWBUFT' #first false
#    myKey = 'KXVMCNOPHQRSZYIJADLEGWBUFT' #right

    myKey3=LETTERS
    while(myKey != myKey3):
        myKey3=myKey
        i=0
        j=25
        m=1
        while (j>0):
            i=0
            while(i<j):
                myKey1=myKey[:i]+myKey[i+m]+myKey[i+1:i+m]+myKey[i]+myKey[i+m+1:]
                score1 = score(encryptMessage(myKey, myMessage))
                score2 = score(encryptMessage(myKey1, myMessage))
                print("Possible key: %s, score:%d" % (myKey1, score2))
                if (score2>score1):
                    myKey=myKey1
                i=i+1
            m=m+1
            j=j-1
   
    
    translated = encryptMessage(myKey, myMessage)
    print "###################################################################"
    print('Using key %s' % (myKey))
    print('Decrypted text:')
    print(translated)
    print "###################################################################"
    print("key: %s, score:%d" % (myKey, score(translated)))


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')
    

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated

'''
#第一次score函数用的频率得分，未考虑低频率的字母，略有错误，遂换频率数据
#双字母组: 
#| TH | HE | IN | ER | AN | RE | ED | ON | 
#| ES | ST | EN | AT | TO | NT | HA | ND | 
#| OU | EA | NG | AS | OR | TI | IS | ET | 
#| IT | AR | TE | SE | HI | OF | 

#三字母组: 
#| THE | ING | AND | HER | ERE | ENT | THA | 
#| NTH | WAS | ETH | FOR | DTH | HAT | SHE | 
#| ION | HIS | STH | ERS | VER | 


def score(message):
    score= message.count("th")*5+message.count("he")*5+message.count("in")*5+message.count("er")*5+ message.count("an")*4+message.count("re")*4+message.count("ed")*4+message.count("on")*4+\
    message.count("es")*3+message.count("st")*3+message.count("en")*3+message.count("at")*3+message.count("to")*3+message.count("nt")*3+message.count("ha")*3+message.count("nd")*3+\
    message.count("ou")*2+message.count("ea")*2+message.count("ng")*2+message.count("as")*2++message.count("or")*2+message.count("ti")*2+message.count("is")*2+message.count("et")*2+\
    message.count("it")+message.count("ar")+message.count("te")+message.count("se")++message.count("hi")+message.count("of")+\
    message.count("the")*5+message.count("ing")*4+message.count("and")*4+message.count("her")*4+message.count("ere")*3+message.count("ent")*3+message.count("tha")*3+\
    message.count("nth")*2+message.count("was")*2+message.count("eth")*2+message.count("for")*2+message.count("dth")*2+message.count("hat")*2+message.count("she")*2+\
    message.count("ion")+message.count("his")+message.count("sth")+message.count("ers")+message.count("ver")+\
    message.count("self")*5
    return score
'''

#use Table 3: English Digram Frequencies [4]
#score= message.count("")+message.count("")+message.count("")+message.count("")+message.count("")+message.count("")+message.count("")+message.count("")+message.count("")+message.count("")

def score(message):
    score = message.count("al")*15+message.count("an")*44+message.count("ar")*14+message.count("as")*12+message.count("at")*20+message.count("av")*5+message.count("ay")*5+\
    message.count("be")*12+message.count("bl")*2+message.count("bo")*2+message.count("br")*2+message.count("bu")*2+message.count("by")*2+\
    message.count("ca")*6+message.count("ce")*6+message.count("ch")*8+message.count("co")*8+\
    message.count("de")*8+message.count("di")*5+message.count("do")*3+message.count("dr")+message.count("ds")*2+message.count("du")+\
    message.count("ea")*12+message.count("ed")*15+message.count("ee")*7+message.count("ei")*4+message.count("el")*8+message.count("em")*6+message.count("en")*20+message.count("er")*20+message.count("es")*16+message.count("et")*8+message.count("ev")*4+message.count("ex")+message.count("ey")*4+\
    message.count("fa")*2+message.count("fe")+message.count("fo")*8+message.count("fr")*3+\
    message.count("ga")+message.count("ge")*4+message.count("go")*4+message.count("gr")*2+\
    message.count("ha")*24+message.count("he")*71+message.count("hi")*18+message.count("ho")*10+message.count("hy")*2+\
    message.count("ic")*5+message.count("id")*5+message.count("ie")*5+message.count("il")*7+message.count("im")*6+message.count("in")*33+message.count("io")*5+message.count("ir")*5+message.count("is")*16+message.count("it")*16+message.count("iv")*3+\
    message.count("ja")+message.count("je")+message.count("jo")+message.count("ju")+message.count("ja")+\
    message.count("ke")*5+message.count("ki")*2+message.count("kn")+\
    message.count("la")*6+message.count("ld")*5+message.count("le")*11+message.count("li")*5+message.count("ll")*14+message.count("lo")*8+message.count("ly")*4+\
    message.count("ma")*8+message.count("mb")+message.count("me")*12+message.count("mm")+message.count("mo")*5+message.count("mp")+message.count("ms")+message.count("mu")+message.count("my")*2+\
    message.count("nc")*4+message.count("nd")*35+message.count("ne")*10+message.count("ng")*14+message.count("ns")*5+message.count("nt")*13+message.count("ny")+\
    message.count("oa")+message.count("ob")+message.count("oc")+message.count("od")*4+message.count("of")*21+message.count("ok")+message.count("ol")+message.count("om")*8+message.count("on")*19+message.count("oo")*3+message.count("op")*2+message.count("or")*20+message.count("os")*3+message.count("ot")*7+message.count("ou")*19+message.count("ov")*2+message.count("ow")*6+\
    message.count("pa")*3+message.count("pe")*5+message.count("ph")+message.count("pi")+message.count("pl")*3+message.count("po")*3+message.count("pp")+message.count("pr")*4+message.count("pt")+message.count("pu")+\
    message.count("qu")+\
    message.count("ra")*7+message.count("re")*75+message.count("ri")*8+message.count("rk")+message.count("rm")+message.count("rn")*2+message.count("ro")*8+message.count("rr")+message.count("rs")*4+message.count("rt")*4+message.count("ru")*2+message.count("rv")+message.count("ry")*2+\
    message.count("sa")*7+message.count("sc")+message.count("se")*15+message.count("sh")*8+message.count("si")*4+message.count("so")*6+message.count("sp")*3+message.count("sr")+message.count("ss")*4+message.count("st")*13+message.count("su")*2+\
    message.count("ta")*5+message.count("te")*11+message.count("th")*85+message.count("ti")*8+message.count("tl")+message.count("to")*17+message.count("tr")*4+message.count("ts")*3+message.count("tt")*2+message.count("tu")*2+message.count("tw")+message.count("ty")*2+\
    message.count("ua")+message.count("ub")+message.count("uc")+message.count("ud")+message.count("ue")+message.count("ug")+message.count("ui")+message.count("ul")*4+message.count("um")+message.count("un")*8+message.count("up")*3+message.count("ur")*7+message.count("us")*7+message.count("ut")*7+\
    message.count("va")+message.count("ve")*14+message.count("vi")*2+\
    message.count("wa")*7+message.count("we")*7+message.count("wh")*8+message.count("wi")*8+message.count("wn")+message.count("wo")*3+\
    message.count("ye")*3+message.count("yo")*3+message.count("ys")
    
    return score


if __name__ == '__main__':
    main()


	
	
	

    
