import itertools

def check_array_sum(numbers):
    if not numbers:
        return False

    max_val = max(numbers)
    numbers_without_max = numbers.copy()
    numbers_without_max.remove(max_val)

    for r in range(1, len(numbers_without_max) + 1):
        for combo in itertools.combinations(numbers_without_max, r): # for each size r we genearate all possible combo of éléments
            if sum(combo) == max_val:
                return True

    return False

