def digital_root(num):
    temp = 0
    while num > 9:
        while (num > 9):
            temp = temp + (num % 10)
            num = num // 10
        num = temp + num
        temp = 0
    return (num)
print(digital_root(1))
for num in range(0, 1000):
    print ("num = ", num, "digital root = ", digital_root(num))

                                                #RECURSIVE
def digital_root_rec(num):
    temp = 0
    while num > 9:
        temp = temp + (num % 10)
        num = num // 10
    temp += num
    return (digital_root(temp)if temp > 9 else temp)
for num in range(0, 1000):
    if digital_root(num) == digital_root_rec(num):
        print ("PASS: ", num, ": ", digital_root(num), " | ", digital_root_rec(num)) 
    else:
        print ("FAILED: ", num, ": ", digital_root(num), " | ", digital_root_rec(num)) 