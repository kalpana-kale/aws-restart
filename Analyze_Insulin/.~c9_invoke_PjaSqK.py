#import re

#Opening a file "preproinsulin-seq-clean.txt" for reading
file_object1 = open("/home/ec2-user/environment/Analyze_Insulin/preproinsulin-seq-clean.txt", "r+")

#print(file_object1.read(), end='\n')

#read()	the file content from "preproinsulin-seq-clean.txt".
txt=file_object1.read()

# Opening a file "lsinsulin-seq-clean.txt" for writing
file_object2 = open("/home/ec2-user/environment/Analyze_Insulin/lsinsulin-seq-clean.txt", "w")

#Get the first 1 to 24 letters from "preproinsulin-seq-clean.txt"
first_24_letters = txt[:24]
print(first_24_letters, end='\n')

#Writes the specified string to the file "lsinsulin-seq-clean.txt"
file_object2.write(first_24_letters)

# Opening a file for appending
#file_object = open("example.txt", "a")


# Opening a file "binsulin-seq-clean.txt" for writing
file_object3 = open("/home/ec2-user/environment/Analyze_Insulin/binsulin-seq-clean.txt", "w")

#Get the first 1 to 24 letters from "preproinsulin-seq-clean.txt"
letters_25_54 = txt[25:54]
print(letters_25_54, end='\n')

#Writes the specified string to the file "binsulin-seq-clean.txt"
file_object3.write(letters_25_54)

# Opening a file "cinsulin-seq-clean.txt" for writing
file_object4 = open("/home/ec2-user/environment/Analyze_Insulin/cinsulin-seq-clean.txt", "w")

#Get the first 1 to 24 letters from "preproinsulin-seq-clean.txt"
letters_55_89 = txt[55:89]
print(letters_55_89, end='\n')

#Writes the specified string to the file "cinsulin-seq-clean.txt"
file_object4.write(letters_55_89)

#Closes the opened file.
file_object1.close()
file_object2.close()
file_object3.close()
file_object4.close()
