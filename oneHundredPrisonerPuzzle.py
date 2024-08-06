# previous outdated attempt; probably won't use

import random
# initilize map set and then randomly pick nums, then delete that num from set and set new limit // could use .shuffle but this is more fun
rand_set = {}

for i in range(1,101):
    rand_set[i] = i
# rand_nums_remaining = 100
random.shuffle(rand_set)


# initialize rand nums in boxes
pris_nums = {}

for i in range(1, 101):
    pris_nums[i] = rand_set[i]
    # pris_nums[i] = rand_set[random.randint(1,(rand_nums_remaining)-i)] 
    # forgot to remove the num from rand_set and then i realized i cant move everything down 
    # rand_nums_remaining -= 1


print(pris_nums)



