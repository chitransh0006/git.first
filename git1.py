row=5
for i in range(row,0,-1):
    for j in range(row,row-i,-1):
        print(j,end="")
    print()