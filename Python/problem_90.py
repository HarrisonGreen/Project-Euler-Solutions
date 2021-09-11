from itertools import combinations

def main():
    digits = [str(x) for x in range(10)]
    count = 0
    
    for cube_one in combinations(digits, 6):
        cube_one = set(cube_one)
        if "6" in cube_one:
            cube_one.add("9")
        if "9" in cube_one:
            cube_one.add("6")
            
        for cube_two in combinations(digits, 6):
            cube_two = set(cube_two)
            if "6" in cube_two:
                cube_two.add("9")
            if "9" in cube_two:
                cube_two.add("6")
            
            if check_squares(cube_one, cube_two):
                count += 1
        
    print(count//2)

def check_squares(cube_one, cube_two):
    squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]
    
    for square in squares:
        if square[0] in cube_one and square[1] in cube_two:
            continue
        if square[1] in cube_one and square[0] in cube_two:
            continue
        return False
    
    return True

if __name__ == "__main__":
    main()
    