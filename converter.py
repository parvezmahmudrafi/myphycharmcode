def find_max(numbers1):
    max = numbers1[0]
    for number in numbers1:
        if number>max:
            max = number

    return max