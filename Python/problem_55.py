def lychrel_count(limit):
    count = 0

    for i in range(1, limit + 1):
        num = i
        for j in range(50):
            num = reverse_add(num)

            if is_palindrome(num):
                break

            if j == 49:
                count += 1

    print(count)

def is_palindrome(x):
    return str(x) == str(x)[-1::-1]

def reverse_add(x):
    return x + int(str(x)[-1::-1])

if __name__ == "__main__":
    lychrel_count(10000)
