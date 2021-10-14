import math

def read_words():
    with open("Data/words.txt") as file:
        for line in file:
            return line.replace("\"", "").split(",")
        
def find_pairs(words):
    n = len(words)
    pairs = []
    
    for i in range(n-1):
        for j in range(i+1, n):
            if sorted(words[i]) == sorted(words[j]):
                pairs.append((words[i], words[j]))
    
    return pairs

def largest_num(pairs):
    top = 0
    for pair in pairs:
        top = max(top, find_square(pair))
        
    print(top)

def find_square(pair):
    k = len(pair[0])
    low = math.ceil(math.sqrt(10 ** (k - 1)))
    high = math.floor(math.sqrt(10 ** k - 1))
    squares = [x ** 2 for x in range(low, high + 1)]
    
    top = 0
    for square in squares:
        values = check_pattern(pair[0], square, k)
        if values:
            num = int("".join([values[pair[1][i]] for i in range(k)]))
            if num in squares:
                top = max(top, square, num)
    
    return top
    
def check_pattern(word, num, k):
    values = {}
    for i in range(k):
        if word[i] in values.keys() and values[word[i]] != str(num)[i]:
            return False
        values[word[i]] = str(num)[i]
        
    if len(set(values.values())) != len(values.values()):
        return False
    
    return values
            
if __name__ == "__main__":
    words = read_words()
    pairs = find_pairs(words)
    largest_num(pairs)
    