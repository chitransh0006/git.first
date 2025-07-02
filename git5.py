n=153
cnt=0
sum=0
for i in str(n):
   i=int(i)
   cnt+=1
for j in str(n):
   j=int(j)
   sum+=pow(j,cnt)   
if sum==n:
   print("armstrong")
else:
   print("not")   
   
   

