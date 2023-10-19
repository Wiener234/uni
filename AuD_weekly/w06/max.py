def search(L, i, j):
    if j-i == 1:
        if L[i] > L[j]:
            return L[i]
        else: 
            return L[j]
    elif i == j:
        return L[i]
    
    m = (i + j)//2

    left = search(L, i, m)
    right = search(L, m+1, j)
    return max(left, right)

print(search([2,9,4,5,8,3,3,9,7], 0, 7))
