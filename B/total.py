def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count



def total2(initial=5, *numbers, **keywords):
    """grdegrdgdgrd"""
    count = initial
    for number in numbers:
        print(number)
    for key in keywords:
        print(keywords[key])
    return count

print(total2.__doc__)