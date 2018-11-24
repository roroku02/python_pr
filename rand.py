import random
import numpy as np

randnum = 0
i = np.zeros(10)
count = 0

while count < 10:
    while randnum != 10:
        rand_int = np.random.rand(15)
        #print('rand_int = ', rand_int)

        randnum = random.randint(0, 1500)
        print('random number =', randnum)
        i[count] += 1

    print("試行回数_", count + 1, ":", i[count])
    randnum = 0
    count += 1

count_avg = sum(i) / 10
print(count_avg)
