
def event_probability(outcomes, sample_space):
    probability = (outcomes / sample_space) * 100
    return round(probability, 1)

num_cards=52
num_ace=4

ace_probablity=event_probability(num_ace,num_cards)

print(str(ace_probablity)+'%')