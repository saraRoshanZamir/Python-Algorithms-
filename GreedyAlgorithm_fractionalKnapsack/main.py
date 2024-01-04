N=7
MAX_WEIGHT=15
objects = [(10,2),(5,3),(15,5),(7,7),(6,1),(18,4),(3,1)]

class Item:
    def __init__(self,profit, weight):
        self.profit=profit
        self.weight=weight
        self.profit_by_weight=profit/weight
        self.portion=0.0

def get_items(n,input_items=None, verbos=0):
    items=[]
    if input_items==None:
        for i in range(n):
            print(f"Items #{i+1}")
            item_profit=int(input("please enter the profit of the item"))
            item_weight=int(input("please enter the weight of the item"))
            items.append(Items(item_profit,item_weight))
            print("______________________________")
    else:
        for item in input_items:
            items.append(Item(item[0],item[1]))
        if verbos:
            for item in items:
                print(f" items  profit:#{item.profit} weight:{item.weight}")
        return items

# highest profit by weight
def highest_p_w_item(list_of_items):
    best_item=None
    for i in list_of_items:
        if best_item:
            if i.profit_by_weight>best_item.profit_by_weight and i.portion<1:
                best_item=i
        else:
            if i.portion<1:
                best_item=i
    return best_item
    
if __name__=="__main__":
    print(f"max weight is :#{MAX_WEIGHT}")
    print("______________________________")
    items=get_items(N,input_items=objects, verbos=0)
    bag=[]
    free_space=MAX_WEIGHT
    while free_space>0:
        best_case=highest_p_w_item(items)
        if best_case:
            if best_case.weight<=free_space:
                best_case.portion=1
                bag.append(best_case)
                free_space-=best_case.weight
            else:
                best_case.portion=((free_space*100)/best_case.weight)/100
                bag.append(best_case)
                free_space=0          
        else:
            break
       
    total_profit=0
    weights=''
    profits=''
    for i in (bag) :
        total_profit+=i.portion*i.profit
        weights+=f"{i.weight*i.portion}+"
        profits+=f"{i.profit*i.portion}+"
        
    print("total_profit:",total_profit)
    print(f"weights:{weights[:len(weights)-3]}")
    print(f"profits:{profits[:len(profits)-3]}")
    