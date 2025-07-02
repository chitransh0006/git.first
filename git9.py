n=1221
oldn=n
rev=0
for i in range(n):
    ld=n%10
    rev=rev*10+ld
    n=n//10
if oldn==rev:
      print("yes")
else:
    print("no")        
  
