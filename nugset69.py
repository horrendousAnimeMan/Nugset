import array
import copy

def rev(a):
    r=[]
    n=len(a)-1
    while n >= 0:
        r.append(a[n])
        n-=1
        #
    #
    return r
#
def ordAr(a):
    n=0
    r=[]
    while n < a:
        r.append(n)
        n+=1
        #
    #
    return r
#
def sw(a,e1,e2):
    r=copy.copy(a)
    #print("sw")
    try:
        #
        r[e1]=a[e2]
        r[e2]=a[e1]
        return r
    except IndexError as er:
        #
        print("in sw, IndexError. e1, e2=",e1,",",e2)
        return a
    #
#
def numSet(a):
    #
    valid=[]
    valid.append(a)
    n=1
    solved=False
    cV=valid[0]
    lea=len(a)
    #print(lea)
    ops=lea*(lea-1)
    op=1
    #print(a)
    #print("init: valid=",valid,"n=",n,"a=",a)

    try:
        while solved==False:
            if op==ops-1: #op==ops is full circle.
                #
                #print("solved.")
                solved=True
            #
            if n<=lea-1:
                #
                nV=sw(cV,0,n)
                valid.append(nV)
                n+=1
                cV=nV
                op+=1
                #print("nV<lea.",nV)
            elif n==lea:
                #
                n=1
                #print("n=",n,"lea=",lea)
                #
            #
        #
    except IndexError as err:
        print(err)
        #print(n)
        #
    #
#
    #print(valid)
    #print("length of valid: ",len(valid))
    #print("operation complete in " ,op," array accesses.") #debug
    return valid
#

def makeIndexes(a):
    if a==0:
        print("zero value for indices 00458568203485")
        return None
    oa=ordAr(a)
    roa=rev(oa)
    noa=numSet(oa)
    rnoa=numSet(roa)
    nT=noa+rnoa
    #print(nT) #debug
    #print("combinations of oa " ,oa, "=",len(nT)) #debug
    #
    return nT
#
