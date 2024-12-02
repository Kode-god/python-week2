# Create an empty list
my_list = []

#appending the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting new numbers
my_list.insert(1, 15)

#extending the list
my_list.extend([50, 60, 70])

#removing the last number in the list 
my_list.pop()

#sorting the list in ascending order
my_list.sort()

#finding and printing the index of 30
index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")
