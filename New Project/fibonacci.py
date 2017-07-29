p = 1
c = 2
sum = 0

while c <= 1000:
    if c % 2 == 0:
        sum += c
print (sum)
for i in range(4000000):
    a = p
    p = c
    c += a
    print (c)
if c % 2 == 0:
    sum += c
    print (sum)
