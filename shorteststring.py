def shorteststring(abc):
    minv = float('inf')
    for i in abc:
        if len(i)<minv:
            minv = len(i)
            index = i
    return index
kk = ['apsfsdsfdasdfple', 'banana', 'tt','saklsjdflkasjdflkasjdflkajs']
print(shorteststring(kk))
