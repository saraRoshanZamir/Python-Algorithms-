def fittnes(population_list,n):
    length=len(population_list)
    for i in range (length):
        conflict=0
        for j in range(n):
            for k in range(j+1,n):
                if population_list[i][j]==population_list[i][k]:
                    conflict+=1
                    
                ###
                if abs(j-k)==abs(population_list[i][j]-population_list[i][k]):
                    conflict+=1
        population_list[i][-1]=conflict
    return population_list
