# Write python code to add additional text to the existing file on a new
# line without deleting the previous contents

file=open("Fileprogram.txt",'a')
file.write("I am an Embedded System Engineer!!")
file.close()

file=open("Fileprogram.txt",'r')
print(file.read())
file.close()
