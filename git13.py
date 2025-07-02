n=18
sum=0
for i in str(n):
    i = int(i)
    sum+=i
print(sum)
if(n%sum==0):
    print("harshad")
else:
    print("not")        