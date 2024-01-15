first_name = "Jose"
last_name ="Portilla"
extra_list_item ="New word"

print (f"Hello {first_name} {last_name}")

my_list = ["First word", "second word", first_name, last_name]

print (my_list)

my_list.insert(1, extra_list_item)

print (my_list)

removed_item= my_list.pop(3)

print(my_list)

print(removed_item)

my_list.reverse()

print(my_list)

my_list.sort(reverse=True)

print(my_list)