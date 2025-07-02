n=456123
even=0
odd=0
for i in str(n):
    i=int(i)
    if i%2==0:
        even += 1
    else:
        odd += 1
    i=i//10
print("even",even,"odd",odd)
   
   


