#create a new file
New_file=open("newfile.txt","x")
New_file.close()

#check if a file exists
import os
print("checking if myfile exists or not....")
if os.path.exists("code.txt"):
    os.remove("code.txt")
else:
    print("The file does not exist")
    #create a new file if it don't exist
    myfile=open("zoe.txt","w")
myfile.write("hi my name is joesph and i am 1years old.")
    myfile.close()

    #delete a file named zoe
    os.remove("zoe.txt")

    # delete the folder
    os.rmdir(" folder")