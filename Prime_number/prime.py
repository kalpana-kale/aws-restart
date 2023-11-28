#Display all the prime numbers between 1 to 250.
# Python3.6  
# Coding: utf-8  

import os
#print(os.getcwd())
#Change directory path
path = '/home/ec2-user/environment/aws-restart/Prime_number'
os.chdir(path)
#print(os.getcwd())

#function to check the number is prime or not
def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

#create empty list
new_list = list()
for n in range(0,250):
    if is_prime(n):
        if n==97:
            new_list.append(n)
        else:
            new_list.append(n)
            new_list.append(" ")

new_str = ''.join(str(e) for e in new_list)
print(new_str)

# Open file in write mode
file_object = open('results.txt', 'w')

file_object.write(new_str)

file_object.close()