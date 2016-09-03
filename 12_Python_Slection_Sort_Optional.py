import random
from time import time

start_time = time()

def selection_sort(lst):

    idx = range(len(lst))
    for i in idx:
        current = idx[i]
        print("Current is: {}".format(current))
        for j in idx:
            check = idx[j]
            print("Check is {}".format(check))
            if lst[i]<lst[j]:
                print("hit")
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    print lst

def rand(num):
    random_list = random.sample(xrange(10000), num)
    return random_list

selection_sort(rand(100))

end_time = time()
time_taken = end_time - start_time # time_taken is in seconds

print("\n")
print("-"*80)
print("This selection sort algorithm took: {} seconds to complete.".format(time_taken))
print("-"*80)
