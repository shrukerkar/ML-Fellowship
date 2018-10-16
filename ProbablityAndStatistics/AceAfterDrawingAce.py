
def event_probability(outcomes, sample_space):
    probability = (outcomes / sample_space) * 100
    return round(probability, 1)

num_cards_after_drawing_ace=51
num_ace_after_drawing_first_ace=3

ace_probablity=event_probability(num_ace_after_drawing_first_ace,num_cards_after_drawing_ace)

print(str(ace_probablity)+'%')