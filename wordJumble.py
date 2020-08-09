import nugset69
import random

def sentenceJumble(a):
    #take source string, "something like this"
    #return string "this like something" or "like this something"
    #possible use of nugset.py on this one.
    #returning all possible paragraphs would be pretty interesting.
    #if just for novelty.  or whatever this is for.
    #
    fp=open(a,'r')
    print("fp=",fp)
    #res
    rStr=fp.read()
    print("rStr=",rStr)
    sStr=rStr.split()
    random.shuffle(sStr) #haha this is cool
    print("len(sStr)=",len(sStr))
    sLen=len(sStr)
    if sLen != 0:
        indexes=nugset69.makeIndexes(sLen)
    #
    newWords=""
    j=0
    
    pat=[8,8,5,5,8] #number of words/syllables(later) for each line. pat[w]
    while j<len(indexes):
        k=0
        w=0 #used for keeping track of word count for pentameter
        tw=0 #used for iterative word count
        while k<sLen:
            newVal=sStr[indexes[j][k]]
            newWords+=newVal
            #count syllables here,tw+=syllables
            syla=syllableCount(newVal)
            newWords+=" "
            k+=1
            tw+=syla
            #
            if tw%pat[w]==0 or tw>pat[w]:
                newWords+="\n"
                tw=0
                if w+1 < len(pat):
                    w+=1
                elif w+1 >= len(pat):
                    w=0
                    newWords+="\n"
                #
            #
        #
        j+=1
        newWords+="\n\n"
        #
    #
    sNw=str(newWords)
    #print(sNw)
    fp.close()
    al=random.randint(1,666)
    nfn="jumbleJel"+str(al)+".txt"
    nfp=open(nfn,'w')
    nfp.write(sNw)
    print("file complete:",nfn)
    nfp.close()
    return None
    '''
    okay, so the logic.
    the index array goes like this: indexes[a[b]] where:
    a is a list,
    b is the element of that list.
    for(a=0;a<indexes.length;a++){
        for(b=0;b<a.length;b++){
            
        }
    }
    -=-=-=-=--=-=-=-=-
    new[a[b]]=indexes[a[b]]
    =-=-==-=-
    o=[0,1,2,3],[0,1,2,3]
    n=[1,2,3,0],[2,3,0,1]
    =-=-=-=-=-=
    for each entry in Words,
    newWords receives the word at Index[a]
    
    '''

##    for j in indexes:
##        for i in sStr:
##            newVal=sStr[indexes[j[i]]]
##            newWords.append(newVal)
    #fp.write(str(res))
    #print(fp)

#
def syllableCount(a):
    #count the syllables in a word.
    #consonant, followed by vowel, until consonant.
    #CHALLENGE: True Syllable Matching.
    #   main challenge: silent and double-vowel e's.
    #   SOLUTION: recognized patterns in which double vowel and silent e is used
    #       "take", "some", "one", "knife", "eight", "use", "alleviate",
    #       "impede", "slice", "ice", "each", "enough", "iteration"
    #       PATTERN:
    #           Vowel-Consonant-E=Silent E, -1 syllable.
    #           E followed by or preceded by I, A, or E = -1 syllable
    #           O followed by or preceded by U = -1 syllable
    vowels={'a','e','i','o','u','y'}
    syl=1
    m=0
    vowelCount=0
    while m < len(a):
        if a[m] in vowels:
            vowelCount+=1
            #
        m+=1
        #
    #
    #UNLESS: adjust syllable count based on defined patterns
    def silentCount(a):
        #a="word"
        #returns number of syllables to deduct from word
        deduct=0
        n=0
        knownSilents=['ion','ize','ate','ou','ie','ei',
                      'ice','take','are','ale',
                      'une','upe','more','oa','ea',
                      'zine','nce','oke','aves','oo',
                      'woo','goo','grain','ee','one','qu','ue',
                      'eye','ide','ee']
        #knownExceptions={}
        while n<len(knownSilents):
            #
            if knownSilents[n] in a:
                deduct+=1
                n+=1
                #
            #
            else:
                n+=1
                #
            #
        #
        return deduct
    #
    syl=vowelCount-silentCount(a)
    return syl
    
#
sentenceJumble('jomble.txt')
#nugset69.makeIndexes(8) #okay it works

    
