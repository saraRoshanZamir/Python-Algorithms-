
from parameters import rAndC
from show import show
from find_index import find_index

def is_check(population_list):
    length=len(population_list)
    directions=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for x in range (length):
        conflict=0
        possible_moves=[]
        find_Queen=find_index(population_list[x],1)
        find_myKing=find_index(population_list[x],2)
        find_OtherKing=find_index(population_list[x],3)
        if find_Queen[0] == find_OtherKing[0]:
            conflict+=1  
        if find_Queen[1] ==find_OtherKing[1]:
            conflict+=1    
        if abs(find_Queen[0]-find_OtherKing[0])==abs(find_Queen[1]-find_OtherKing[1]):
            conflict+=1  
        population_list[x][-2]=conflict
        if conflict>0:
            for y in  directions:
                new_pos = (find_OtherKing[0] + y[0], find_OtherKing[1] + y[1])
                if not new_pos == find_myKing:
                    if 0 <= new_pos[0] < rAndC and 0 <= new_pos[1] < rAndC:
                        possible_moves.append(new_pos)

            for m in possible_moves:
                ismate=0
                if find_Queen[0] == m[0]:
                    
                    ismate+=1  
                if find_Queen[1] ==m[1]:
                    ismate+=1    
                if abs(find_Queen[0]-m[0])==abs(find_Queen[1]-m[1]):
                    ismate+=1
                if ismate== len(possible_moves):
                    population_list[x][-1]='1'
        if population_list[x][-1]=='1':            
            show(find_Queen,find_myKing,find_OtherKing)
            break
                    
                
                
    return population_list

    
    