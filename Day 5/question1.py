sub_list=[1,1,5]
listy = [1,5,6,4,1,2,3,5]
temp=0
m=0
for i in range(len(listy)):
    m=m+1
    if(listy[i]==sub_list[temp]):
        temp=temp+1
        if(temp==3):
            print("it is a Match")
    else:
        if(m==len(listy)):
            print("Gone")



sub_list=[1,1,5]
listy = [1,5,6,5,1,2,3,6]
temp=0
m=0
for i in range(len(listy)):
    m=m+1
    if(listy[i]==sub_list[temp]):
        temp=temp+1
        if(temp==3):
            print("it is a Match")
    else:
        if(m==len(listy)):
            print("it is Gone")
        
        


    
        
        
        




