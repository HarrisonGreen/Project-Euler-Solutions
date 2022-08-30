def main():
    limit = 200
    m = {1: 0}
    
    groups = set()
    groups.add((1,))
    
    i = 0
    while True:
        i += 1
        new_groups = set()
        
        for group in groups:
            for a in group:
                for b in group:
                    if a + b > limit or a + b <= max(group):
                        continue
                    else:
                        new_groups.add(group + (a + b,))
                        if a + b not in m.keys():
                            m[a + b] = i
                            if len(m) == limit:
                                return sum(m.values())
                        
        groups = new_groups
        
print(main())
