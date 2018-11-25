import json
import requests


def add(a, b):
    sum_num = a + b
    print(sum_num)


x = 10000
y = 2
add(x, y)

res = requests.get('https://training.spjservice.com/python/level1/fluits.json')
data = json.loads(res.text)
print(data)
price_sum = sum(int(x['price']) for x in data)
print(price_sum)
