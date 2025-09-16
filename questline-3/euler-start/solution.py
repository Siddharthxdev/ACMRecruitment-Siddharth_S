#Problem 1
i = 0
j = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        j = j + i
    i = i + 1
print(j)


# Problem 2
t = 1
k = 2
for  i in range(10):
    t = t + k
    print(t,end = ' ')
    t = k
    k = t
