# Question 1 

land_plane = int(input("Enter Plane landing fit: "))

if(land_plane<=1000):
    print("Safe to Land")
elif(land_plane>1000 and land_plane<5000):
    print("Bring down to 1000")
else:
    print("Turn Around")

# Question 2

for i in range(2,201): 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 

