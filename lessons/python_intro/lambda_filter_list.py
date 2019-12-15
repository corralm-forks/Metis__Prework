# The very last step is that it that you set f to a function, and you're currently 
# setting it to a list. This function should input my_list and output what you already have.

# f = list(filter(lambda x: (x % 2 == 0), my_list))

my_list = [3, 4, 7, 2, 9, 170]

# This worked as a function for Q.14
f = lambda my_list: filter(lambda x: (x % 2 == 0), my_list)

for x in f(my_list):
    print(x)

# def filter_list(arg):
#     for i in arg:
#         if i % 2 == 0:
#             print(i)

# filter_list(my_list)      
# for i in filter_list(my_list):
#     print(i)
