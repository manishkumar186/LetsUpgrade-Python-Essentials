first_number = 1042000
last_number = 702648265

for i in range(first_number,last_number+1):
    qube = len(str(i))
    temp = i
    sum=0

    while(temp>0):
        digit = temp % 10
        sum = sum + digit**qube
        temp = temp//10
    if(i == sum):
        print("The first armstrong nyumber is ",i)
        break



    

