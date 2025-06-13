import re

def add(number: str) -> int:
    if(not number):
        return 0
    delimeter = ','

    numbers = re.split(delimeter, number)
    num_list = list(map(int, filter(None, numbers)))

    negatives = [n for n in num_list if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

    return sum(num_list)
