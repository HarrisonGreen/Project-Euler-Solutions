from math import factorial

def read_files():
    beds = []
    desks = []
    
    for line in open("Data/beds.txt"):
        line = line.strip().split(",")
        line = [int(x) for x in line]
        beds.append(line)
        
    for line in open("Data/desks.txt"):
        line = line.strip().split(",")
        line = [int(x) for x in line]
        desks.append(line)
        
    return beds, desks

def count_groups(beds, desks, students):
    even_closed = {}
    even_open = {}
    odd_open_bed = {}
    odd_open_desk = {}
    remaining = [i for i in range(1, students + 1)]
    
    while beds:
        chain = beds[0]
        beds = beds[1:]
        
        found = True
        while found:
            found_desk, chain, desks = find_pair(chain, desks)
            found_bed, chain, beds = find_pair(chain, beds)
            found = found_desk or found_bed
                
        n = len(chain) - 1
        if n % 2 == 1:
            if found_desk and not found_bed:
                odd_open_desk[n] = odd_open_desk.get(n, 0) + 1
            else:
                odd_open_bed[n] = odd_open_bed.get(n, 0) + 1
        elif chain[0] == chain[-1]:
            even_closed[n] = even_closed.get(n, 0) + 1
            chain = chain[:-1]
        else:
            even_open[n] = even_open.get(n, 0) + 1
            
        for student in chain:
            remaining.remove(student)
            
    for pair in desks:
        odd_open_desk[1] = odd_open_desk.get(1, 0) + 1
        remaining.remove(pair[0])
        remaining.remove(pair[1])
        
    singles = len(remaining)
    
    return even_closed, even_open, odd_open_bed, odd_open_desk, singles
    
def find_pair(chain, pairs):
    found = False
    
    for pair in pairs:
        if pair[0] == chain[-1]:
            chain.append(pair[1])
            found = True
            break
        if pair[1] == chain[-1]:
            chain.append(pair[0])
            found = True
            break
        if pair[0] == chain[0]:
            chain = [pair[1]] + chain
            found = True
            break
        if pair[1] == chain[0]:
            chain = [pair[0]] + chain
            found = True
            break
        
    if found:
        pairs.remove(pair)
        
    return found, chain, pairs

def count_permutations(even_closed, even_open, odd_open_bed, odd_open_desk, singles):
    total = 1
    m = 999999937
    
    for length, count in even_closed.items():
        total = (total * factorial(count)) % m
        total = (total * (length ** count)) % m
        
    for count in even_open.values():
        total = (total * factorial(count)) % m
        
    for count in odd_open_bed.values():
        total = (total * factorial(count)) % m
        total = (total * (2 ** count)) % m
    
    for count in odd_open_desk.values():
        total = (total * factorial(count)) % m
        total = (total * (2 ** count)) % m
        
    total = (total * factorial(singles)) % m
    
    print(total)

if __name__ == "__main__":
    beds, desks = read_files()
    students = 500
    
    even_closed, even_open, odd_open_bed, odd_open_desk, singles = count_groups(beds, desks, students)
    count_permutations(even_closed, even_open, odd_open_bed, odd_open_desk, singles)
    