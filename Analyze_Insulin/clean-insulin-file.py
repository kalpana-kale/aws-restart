# Python3.6  
# Coding: utf-8  
import re
import os
#print(os.getcwd())
#Change directory path
path = '/home/ec2-user/environment/aws-restart/Analyze_Insulin'
os.chdir(path)
#print(os.getcwd())


#Opening a file "preproinsulin-seq-clean.txt" for reading
file_object1 = open("preproinsulin-seq.txt", "r")


txt = file_object1.read()
print(txt, end='\n\n')
new_str = re.sub("[^a-z]","",txt)
result = new_str

'''
#read()	the file content from "preproinsulin-seq.txt".
txt = file_object1.read().replace("\n","")
print(txt, end='\n\n')
#It may not be as fast, but why not use Regex to remove the characters/phrases
new_str = re.compile(r"(O|R|I|G|I|N|" "|1|61|//|' ')")
result = new_str.sub('', txt.replace(" ",""))
'''

# Opening a file "lsinsulin-seq-clean.txt" for writing
file_object2 = open("preproinsulin-seq-clean.txt", "w")

#Writes the specified string to the file "lsinsulin-seq-clean.txt"
file_object2.write(new_str)
print("preproinsulin-seq-clean.txt: ", new_str, end='\n')

#Closes the opened file.
file_object1.close()
file_object2.close()

