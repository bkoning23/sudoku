'''
Created on Apr 18, 2014

@author: Brendan
'''

list = input("Type the first row:")

if(len(list) != 9):
    print("list is not 9 digits long")
for i in range(9):    
    for j in range(len(list)):
        rows[i][j] = cell(list[j])