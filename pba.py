rows = int(input("Enter the number of rows: "))  
  
# This will print the rows  
for i in range(1, rows+1):  
    # This will print number of column 
    if (i%2==0):
       for j in range(i,0,-1):
           if j==1:
                print(j, end='')
           else:
                print(j, end='#') 
    else:
        for j in range(1,i+1): 
            if j==i:
                print(j, end='')  
            else:
                print(j, end='#') 
    print("") 