# problem 1: Multiples of 3 and 5
# find the sum of all multiples of 3 and 5 below 1000
# test value: 3, 5, 6, 9 = 23

def multiple_of(check_me):
    five_check = check_me % 5
    three_check = check_me % 3

    if (five_check == 0 or three_check == 0): result = True 
    else: result = False

    return result

print("test, ", multiple_of(7))


