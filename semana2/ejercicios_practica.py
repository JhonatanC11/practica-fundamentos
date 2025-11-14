"""
def count_by(x, n):
    multiplos = []
    for i in range(1, n+1): 
        multiplo = x * i
        multiplos.append(multiplo)
    return multiplos
print(count_by(100, 5))

"""
"""
def find_needle(haystack):
    pos = haystack.index('needle')
    return f"found the needle at position {pos}"

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
"""


def sum_array(arr):
    resul = 0
    if not arr:
        return 0
    for i in arr:
        if i == max(arr) or i == min(arr):
            pass
        else:
            resul += i
    return resul

print(sum_array([1]))