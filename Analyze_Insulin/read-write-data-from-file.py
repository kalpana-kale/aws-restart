# Python3.6  
# Coding: utf-8  
# Read the content of file and replace spaces and other unnecessory characters with nothing(blankspace)

#Opening a file "preproinsulin-seq-clean.txt" for reading
file_object1 = open("/home/ec2-user/environment/aws-restart/Analyze_Insulin/preproinsulin-seq-clean.txt", "r+")

#read()	the file content from "preproinsulin-seq-clean.txt".
txt = file_object1.read()
print(txt)

# Opening a file "lsinsulin-seq-clean.txt" for writing
file_object2 = open("/home/ec2-user/environment/aws-restart/Analyze_Insulin/lsinsulin-seq-clean.txt", "w")

#Get the first 1 to 24 letters from "preproinsulin-seq-clean.txt"
first_24_letters = txt[:24]
print(first_24_letters, end='\n')

#Writes the specified string to the file "lsinsulin-seq-clean.txt"
file_object2.write(first_24_letters)

# Opening a file for appending
#file_object = open("example.txt", "a")

# Opening a file "binsulin-seq-clean.txt" for writing
file_object3 = open("/home/ec2-user/environment/aws-restart/Analyze_Insulin/binsulin-seq-clean.txt", "w")

#Get the first 1 to 24 letters from "preproinsulin-seq-clean.txt"
letters_25_54 = txt[24:54]
print(letters_25_54, end='\n')

#Writes the specified string to the file "binsulin-seq-clean.txt"
file_object3.write(letters_25_54)

# Opening a file "cinsulin-seq-clean.txt" for writing
file_object4 = open("/home/ec2-user/environment/aws-restart/Analyze_Insulin/cinsulin-seq-clean.txt", "w")

#Get the first 1 to 24 letters from "preproinsulin-seq-clean.txt"
letters_55_89 = txt[54:89]
print(letters_55_89, end='\n')


#Writes the specified string to the file "cinsulin-seq-clean.txt"
file_object4.write(letters_55_89)

# Opening a file "ainsulin-seq-clean.txt" for writing
file_object5 = open("/home/ec2-user/environment/aws-restart/Analyze_Insulin/ainsulin-seq-clean.txt", "w")

#Get the first 1 to 24 letters from "preproinsulin-seq-clean.txt"
letters_90_110 = txt[89:110]
#Writes the specified string to the file "ainsulin-seq-clean.txt"
file_object5.write(letters_90_110)
print(letters_90_110, end='\n')


#Closes the opened file.
file_object1.close()
file_object2.close()
file_object3.close()
file_object4.close()
file_object5.close()
