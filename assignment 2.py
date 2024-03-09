# This program creates a list and apppends elements on it
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
my_list.remove(70)
my_list.sort()
index = my_list.index(30)
print("The Index Position of 30 is: ", index)
print("The Current List is: ", my_list)
