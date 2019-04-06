def task1_check(target):
    res = 0
    for num in range(0, target):
        if (num % 3 == 0 or num % 5 == 0):
            res += num
    return res

def task1(target):
    res = 0
    i = 0
    while i * 5 < target:
        res += i * 5
        if ((i * 3) % 5 > 0):
            res += i * 3
        i+=1
    while i * 3 < target:
        if (i * 3) % 5 > 0:
            res += i * 3
        i+=1
    return res
for num in range(0, 1000):
    if task1(num) == task1_check(num):
        print ("PASS: ", num, ": ", task1(num), " | ", task1_check(num)) 
    else:
        print ("FAILED :", num, ": ", task1(num), " | ", task1_check(num))