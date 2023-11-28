# Python3.6  
# Coding: utf-8  
import os
#print(os.getcwd())
#Change directory path
path = '/home/ec2-user/environment/aws-restart/Analyze_Insulin'
os.chdir(path)
#print(os.getcwd())

# Open file in read mode
file = open("preproinsulin-seq-clean.txt", "r")
# Read the content of file and replace spaces with nothing
data = file.read()
print(data)
# Get the length of the data
number_of_characters = len(data)
print('Number of characters in text file "preproinsulin-seq-clean.txt":', number_of_characters, end='\n\n')


# Open file in read mode
file = open("lsinsulin-seq-clean.txt", "r")
# Read the content of file and replace spaces with nothing
data = file.read()
print(data)
# Get the length of the data
number_of_characters = len(data)
print('Number of characters in text file "lsinsulin-seq-clean.txt":', number_of_characters, end='\n\n')

# Open file in read mode
file = open("binsulin-seq-clean.txt", "r")
# Read the content of file and replace spaces with nothing
data = file.read()
print(data)
# Get the length of the data
number_of_characters = len(data)
print('Number of characters in text file "binsulin-seq-clean.txt":', number_of_characters, end='\n\n')

# Open file in read mode
file = open("cinsulin-seq-clean.txt", "r")
# Read the content of file and replace spaces with nothing
data = file.read()
print(data)
# Get the length of the data
number_of_characters = len(data)
print('Number of characters in text file "cinsulin-seq-clean.txt":', number_of_characters, end='\n\n')

# Open file in read mode
file = open("ainsulin-seq-clean.txt", "r")
# Read the content of file and replace spaces with nothing
data = file.read()
print(data)
# Get the length of the data
number_of_characters = len(data)
print('Number of characters in text file "ainsulin-seq-clean.txt":', number_of_characters, end='\n\n')



#close file
file.close()
