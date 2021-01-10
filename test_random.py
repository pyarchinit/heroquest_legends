import random

rn_sum_list = []
for i in range(100):
    value_1 = random.randint(1, 6)
    
    value_2 = random.randint(1, 6)
    
    value_3 = random.randint(1, 6)
    
    value_4 = random.randint(1, 6)
    
    rn_list = [value_1, value_2, value_3, value_4]

    rn_sum_list.append(sum(rn_list))

rn_sum_list.sort()
print(rn_sum_list)

rn_sum_list = []
for i in range(100):
    rng = random.SystemRandom()
    value_1b = rng.randint(1, 6)

    rng = random.SystemRandom()
    value_2b  = rng.randint(1, 6)

    rng = random.SystemRandom()
    value_3b = rng.randint(1, 6)

    rng = random.SystemRandom()
    value_4b = rng.randint(1, 6)

    rn_list = [value_1b, value_2b, value_3b, value_4b]

    rn_sum_list.append(sum(rn_list))

rn_sum_list.sort()
print(rn_sum_list)

