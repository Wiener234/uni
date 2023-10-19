def liRandMax(L,i,j):
    # pre: 0 <= i <= j < len(L)
    # post: maximale Summe einer linken Randfolge
    # der Teilfolge von i bis j (einschließlich i,j)
    max = 0
    sum = 0
    for k in range(i,j+1): # k = i, i+1, ..., j
        sum += L[k]
        if (sum > max):
            max = sum
    return max

def reRandMax(L,i,j):
    # pre: 0 <= i <= j < len(L)
    # post: maximale Summe einer rechten Randfolge
    # der Teilfolge von i bis j (einschließlich i,j)
    max = 0
    sum = 0
    for k in range(j,i-1,-1): # k = j, j-1, ..., i
        sum += L[k]
        if (sum > max):
            max = sum
    return max
    

def maxTeilsumme(L,i,j):
    # pre: 0 <= i <= j < len(L)
    # post: maximale Teilsumme der Teilfolge
    # von i bis j (einschließlich i,j)
    if (i == j): # nur ein Element
        if L[i] > 0: return L[i]
        else: return 0
    else:
        m = (i + j)//2 # Mitte von L
        maxLinks = maxTeilsumme(L,i,m)
        maxRechts = maxTeilsumme(L,m+1,j)
        maxMisch = reRandMax(L,i,m) + liRandMax(L,m+1,j)
        return max(maxLinks, maxRechts, maxMisch)

def maxTeilsumme_rek(L):
# pre: L ist nicht leer
# post: maximale Teilsumme von L
    return maxTeilsumme(L,0,len(L)-1)

print(maxTeilsumme_rek([9,-2,-4,10,6,8,-50]))
