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

