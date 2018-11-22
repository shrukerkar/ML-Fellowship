

#What is the probability of three heads HHH

#import random

#n = 3
#heads = 0
#tails = 0

#for i in range(n):
#    flip = random.randint(1, 8)
#    if flip == 1:                # head
#        heads = heads + 1
#    else:                        # tail
#        tails = tails + 1

#print('Heads:', heads)
#print('Tails:', tails)

import random

def flip_coin():
    return random.choice("HHH")


def flip_coins(n):
    for i in range(n):
        if flip_coins() == "H":
            heads_count +=1

        return heads_count


for i in range (100):
    if flip_coins(3) == "3":
        multiple_heads_count += 1

    return multiple_heads_count


print(multiple_heads_probability)
#print(second_probability)


multiple_heads_probability = multiple_heads_count/100
#second_probability = 56/256