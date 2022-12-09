#!/usr/bin/python3
# MAGALI ANAHI MEZA CHAVEZ
import os 
import time

dictionary = dict()
dictionary2 = dict()
array=[]

#Lists all files in the directory stored in path and stores the file name and date in a dictionary.

for file in os.listdir():
    count = 1
    path = r"/home/user/myscript/" + file
    if path == "/home/user/myscript/lsDir":
    	pass
    else:
        ti_m = os.path.getmtime(path)
        m_ti = time.ctime(ti_m)
        t_obj = time.strptime(m_ti)
        t_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
        dictionary[file] = t_stamp  
        count+=1
    #Validation for no more than 25 files
    if count == 25:
     	break
        
print('\nFiles found: ')
print(dictionary)

#Sorting algorithm QuickSort
def QuickSort(arr):

    elements = len(arr)
    
    #In case there is a single element
    if elements < 2:
        return arr
    
    current_position = 0 #Current position
    
    #Partitioning cycle
    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp #Gives the pivot its proper position in the middle
    
    left = QuickSort(arr[0:current_position]) #Sorts the elements to the left of the pivot
    right = QuickSort(arr[current_position+1:elements]) #Sorts the elements to the right of the pivot

    arr = left + [arr[current_position]] + right #Puts everything together
    
    return arr #Return sorted dates

#Saves dictionary dates in a list
for item in dictionary.values():
   array.append(item)
   
#Save the sorted dates in another list
sortedArray = QuickSort(array)

#For each date in the array of the list with the sorted dates it will look 
# in the dictionary for that date and sort it in another dictionary.

for elm in sortedArray: 
   for key, value in dictionary.items():
   	if elm == value:
   	   dictionary2[key] = elm

print('\nComputer files by date: ')
for key, value in dictionary2.items():
    print(' ', key, '\t     ', value)
