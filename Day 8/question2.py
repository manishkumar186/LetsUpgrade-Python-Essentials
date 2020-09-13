files = open("Day 8/abcd.txt","r")

object = files.read()
print(object)

try:
    files.write("i am a busy person")
    print("file writting successfullly!!!")

except:
    print("You are open file in readmode so you can not write in this file  !!!!")





    
