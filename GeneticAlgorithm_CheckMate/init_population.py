from random import shuffle
def init_population(n,ps):
    population_list=[]
    for i in range(ps):
        member=[]
        for j in range(n-3):
            member.append(0)
        member.append(1)
        member.append(2) 
        member.append(3) 
        shuffle(member)
        population_list.append(member+['none']+['none'])
        
    return population_list
