def cross_over(population_list, n, ps):
    for i in range(0, ps, 2):
        child1 = population_list[i][:n//2] + population_list[i+1][n//2:n] + ['none']+['none']
        child2 = population_list[i+1][:n//2] + population_list[i][n//2:n] + ['none']+['none']
        child1 = fix_values(child1)
        child2 = fix_values(child2)
        population_list.append(child1)
        population_list.append(child2)
    return population_list

def fix_values(arr):
    arr_set = set(arr)
    if 1 not in arr_set:
        arr[arr.index(0)] = 1
    if 2 not in arr_set:
        arr[arr.index(0)] = 2
    if 3 not in arr_set:
        arr[arr.index(0)] = 3
    if arr.count(1) > 1:
        arr[arr.index(1)] = 0
    if arr.count(2) > 1:
        arr[arr.index(2)] = 0
    if arr.count(3) > 1:
        arr[arr.index(3)] = 0
    return arr