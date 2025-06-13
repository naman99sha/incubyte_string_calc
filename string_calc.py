import re

_custom_delimiter_pattern = re.compile(r'\[(.*?)\]')

def add(number: str) -> int:
    if(not number):
        return 0
    delimiter_pattern = ',|\n'

    if number.startswith('//'):
        header, number = number.split('\n', 1)
        delimiter_def = header[2:]
        
        if delimiter_def.startswith('['):
            delimiters = _custom_delimiter_pattern.findall(delimiter_def)
            delimiter_pattern = '|'.join(map(re.escape, delimiters))
        else:
            delimiter_pattern = re.escape(delimiter_def)


    numbers = re.split(delimiter_pattern, number)
    # num_list = list(map(int, filter(None, numbers)))

    total = 0
    negatives = []

    # negatives = [n for n in num_list if n < 0]

    for num in numbers:
        if num == '':
            continue
        num_int = int(num)
        if num_int < 0:
            negatives.append(num_int)
        else:
            total += num_int
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
    return total
