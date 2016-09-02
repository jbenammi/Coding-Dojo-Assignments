import random

def bubble_sort(lst):


    idx = range(len(lst) -1)
    while sorted(lst) != lst:
        for i in idx:
            if lst[i]>lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    else:
        print lst


def rand(num):
    random_list = random.sample(xrange(1000), num)
    return random_list

bubble_sort(rand(100))
