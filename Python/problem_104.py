import math

def check_first_digits(limit, cut_off):
    nums = (1, 1, False)
    valid = []

    for i in range(3, limit + 1):

        if nums[2]:
            num = nums[1] + int(str(nums[0])[:-1])
        else:
            num = nums[1] + nums[0]

        if check_pandigital(str(num)[:9]):
            valid.append(i)

        if len(str(num)) > cut_off:
            nums = (nums[1], int(str(num)[:-1]), True)
        else:
            nums = (nums[1], num, False)

    return valid

def check_last_digits(limit):
    nums = (1, 1)
    valid = []

    for i in range(3, limit + 1):

        num = str(nums[0] + nums[1])[-9:]

        if check_pandigital(num):
            valid.append(i)

        nums = (nums[1], int(num))

    return valid

def check_pandigital(num):
    for i in range(1, 10):
        if str(i) not in num:
            return False
    return True

if __name__ == "__main__":
    limit = 500000
    start = check_first_digits(limit, 20)
    end = check_last_digits(limit)

    for num in start:
        if num in end:
            print(num)
