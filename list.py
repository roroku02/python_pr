import random

rand_num = [random.randint(0, 100) for i in range(20)]
print([x**2 for x in rand_num])

text_array = ['conputer', 'tv', 'work', 'desk']
text_comma = ','.join(text_array)
print(text_comma)

text_normal = text_comma.split(',')
print(text_normal)
