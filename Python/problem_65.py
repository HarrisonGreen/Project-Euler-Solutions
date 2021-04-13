def continued_fraction(num_terms):
    cont_frac = [2]
    for i in range(1, num_terms):
        if i % 3 == 2:
            cont_frac.append(int((i + 1) * 2/3))
        else:
            cont_frac.append(1)
            
    return cont_frac

def evaluate_fraction(num_terms, cont_frac):
    numr, denr = cont_frac[-1], 1
    for i in range(num_terms - 1):
        numr, denr = cont_frac[-i - 2] * numr + denr, numr
        
    print(sum(int(d) for d in str(numr)))

if __name__ == "__main__":
    num_terms = 100
    cont_frac = continued_fraction(num_terms)
    evaluate_fraction(num_terms, cont_frac)
