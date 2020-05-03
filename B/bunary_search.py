def binary_search(my_list, item):
    low = 0
    high = len(my_list)-1

    while low <=high:
        mid = int((low+high)/2)
        guess = my_list[mid]
        if guess == item:
            print(mid)
            return mid
        elif guess>item:
            high = mid -1
        else:
            low = mid +1
    return None

binary_search([1,2,6,7,8,11,13,16,18], 18)
