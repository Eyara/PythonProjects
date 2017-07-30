p = 1 
c = 2 
sum = 0
while c <= 4000000: 
    if c % 2 == 0: 
        sum += c  
    a = p 
    p = c 
    c += a 
print (sum)
