import string
import random
def append_elem(arr, str):
    word_len = len(str)
    leng = len(arr[word_len])
    for i in range(0, leng - 1):
        if (arr[word_len][i] > str):
            arr[word_len].insert(i, str)
            return 
    arr[word_len].append(str)
    return

def sort_string(arr):
    res = {}
    
    for ch in arr:
        if not type(ch) is str:
            return (arr)
        if len(ch) not in res:
            res[len(ch)] = [ch]
        else:
            append_elem(res, ch)
    i = 0
    for key, value in sorted(res.items()):
        for ch in value:
            arr[i] = ch
            i+=1
    return (arr)
        

def check_sort(arr):
    prev = 0
    for str in arr:
        leng = len(str)
        if (prev > len(str)):
            return (" : FAIL")
        prev = leng
    return (": PASS")

def lst_generator(words_number = 20,word_len = 10):
    res = []
    for _ in range(0, words_number):
        res.append(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(0, random.randint(0, word_len))))
    return res
for num in range(0, 100):
    print '\t\t\t\t\t\t\t\t\t\t\t\t\t\t', num
    arr = lst_generator(30, 16)
    # arr = [(random.randint(0, 12)) for _ in range(0, 10)]
    arr_copy = arr
    arr_copy.sort(key=len)
    if check_sort(arr):
        print '|---------------------------------------------|\nPASS:\n',sort_string(arr),'\n\n' ,arr_copy, '\n|---------------------------------------------|\n'
    else:
        print '|---------------------------------------------|\nFAILED:\n', sort_string(arr),'\n\n',arr_copy, '\n|---------------------------------------------|\n'