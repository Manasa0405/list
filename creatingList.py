a=[1,2,3,4,5,6,7,8,9,0]
print(a)
empty_list = []
print(empty_list)
mixed_list = [1,'two',3.0,'a',5]
print(mixed_list)

# modifying the list
a[3]=30
print(a)

#adding elements to the list
a.append(40)
print(a)

#removing elements
a.remove(40)
print(a)

#List functions
print(len(a)) #length of the list
print(max(a)) #Maximum value in the list
print(min(a)) #minimum value in the list
print(sum(a)) #sum of the elements in the list
print(sorted(a)) #sorted list
print(a.count(1)) #count of occurance of one in the list
print(a.index(3)) #indux of the first occurance of the element in the list

# Reversing the list
a.reverse()
print(a) # print the reversed list

#Slicing the list
print(a[2:5]) #prints elements from index 2 to 4
print(a[:5]) # prints elements from start to index 4
print(a[5:]) # print elements from index 5 to end
print(a[-1]) #print the last elements in the list
print(a[-4]) #print element from the end of 4th index

# list comprehension
squared_list =[x**2 for x in a if x%2==0]
print(squared_list) # prints the square of the elements in the list
