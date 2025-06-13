import re

def add(number: str) -> int:
    if(not number):
        return 0
    delimeter = ','

    numbers = re.split(delimeter, number)
    num_list = list(map(int, filter(None, numbers)))

    return sum(num_list)
