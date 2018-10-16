
def event_probability(outcomes, sample_space):
    probability = (outcomes / sample_space) * 100
    return round(probability, 1)

num_cards_after_drawing_king=51
num_ace=4

ace_probablity=event_probability(num_ace,num_cards_after_drawing_king)

print(str(ace_probablity)+'%')