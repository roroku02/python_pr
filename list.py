import random

my_list = []

for i in range(20):
    my_list.append(random.randint(0, 200))

print('normal_list::')
print(my_list)

my_list = map(lambda x: x * x, my_list)
print('square_list::')
print(list(my_list))

my_list = list(filter(lambda x: x <= 2000, my_list))
print('filter 2000::')
print(list(my_list))
