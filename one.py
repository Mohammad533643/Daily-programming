# We wanna order the nubers from lesser to bigger

# Fisrt we get some number from user and put in a list
x = list(map(float,input().split()))

# Then build a empty list
n = len(x)*[0]

# Finally, we perform the operation 
for i in range(len(x)):
    c = min(x)
    n[i] += c
    x.remove(c)
    c = 0

print(*n)