x = list(map(int,input().split()))
sum = 0
for i in x:
    if i%3==0:
        sum = sum+i
    elif i%5==0:
        sum = sum+i
print(sum)
