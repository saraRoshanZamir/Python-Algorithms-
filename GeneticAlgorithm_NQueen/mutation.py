from random import shuffle
from random import randint as rnd

def mutation(population_list,n,ps,mr):
    choosen_ones=list(range(ps,ps*2))
    shuffle(choosen_ones)
    choosen_ones= choosen_ones[:int(ps*mr)]
    
    for i in choosen_ones:
        cell=rnd(0,n-1)
        val=rnd(0,n-1)
        population_list[i][cell]=val
    return population_list     