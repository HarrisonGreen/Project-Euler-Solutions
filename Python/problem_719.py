import numpy as np

def sum_set(n, split):
    if len(str(n)) == 1:
        if split == True:
            return {}
        else:
            return {n}
    
    full_set = set()
    if not split:
        full_set.add(n)
    
    for i in range(1, len(str(n))):
        right_set = sum_set(int(str(n)[i:]), False)
        right_set = {int(str(n)[:i]) + x for x in right_set}
        
        full_set = full_set.union(right_set)
                
    return full_set
        
if __name__ == "__main__":
    lim = 10**12
    total = 0
    
    for i in range(4, int(np.sqrt(lim)) + 1):
        if i in sum_set(i**2, True):
            total += i**2
            
    print(total)