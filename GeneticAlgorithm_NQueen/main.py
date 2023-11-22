from parameters import *
from initial_population import init_population;
from cross_over import cross_over;
from mutation import mutation;
from fittness import fittnes;
from show import show



current_population=init_population(N,Ps)
current_population=fittnes(current_population,N)
current_population=sorted(current_population, key=lambda x:x[-1])
if current_population[0][-1]==0:
    print("solution found in init population:", current_population[0])
    show(current_population[0],N)

else:
    for i in range(Epoch):
        current_population=cross_over(current_population,N,Ps)
        current_population=mutation(current_population,N,Ps,Mr)
        current_population=fittnes(current_population,N)
        current_population=sorted(current_population, key=lambda x:x[-1])
        current_population=current_population[:Ps]
        if current_population[0][-1]==0:
            print(i+1,"th try:","solution found:", current_population[0])
            show(current_population[0],N)
            break
        else:
            print("best solution so far:", current_population[0])
    else:
        print('sorry we couldnt found a solution')
        