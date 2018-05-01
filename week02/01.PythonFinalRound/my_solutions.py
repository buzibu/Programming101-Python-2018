

# 1. Is Number Balanced?
def is_number_balanced(number):
    number = str(number)
    left = number[:len(number)//2]
    if len(number)%2:
        right = number[len(number) // 2 + 1:]
    else:
        right = number[len(number)//2:]
    # print(left)
    # print(right)
    if sum([int(x) for x in left]) == sum([int(y) for y in right]):
        return True
    else:
        return False


# 2. Increasing and Decreasing Sequences
def increasing_or_decreasing(seq):

    up_check = True
    for i in range(len(seq)- 1):
        up_check = up_check and seq[i] < seq[i + 1]

    down_check = True
    for i in range(len(seq)- 1):
        down_check = down_check and seq[i] > seq[i + 1]

    if down_check:
        return "Down!"
    elif up_check:
        return "Up!"
    else:
        return False


# 3. Largest Palindrome


# check for palindrome
def is_palindrome(number):
    number = str(number)
    left = number[:len(number)//2]
    if len(number)%2:
        right = number[len(number) // 2 + 1:]
    else:
        right = number[len(number)//2:]
    if left == right[::-1]:
        return True
    else:
        return False


def get_largest_palindrome(n):
    palindromes = []
    for i in range(n):
        if is_palindrome(i):
            palindromes.append(i)
    return max(palindromes)


# 4. Sum all numbers in a given string
def sum_of_numbers(input_string):
    input_l = list(input_string)
    output_l = []
    small_list = []
    for ch in input_l:
        if ch.isdigit():
            small_list.append(ch)
        elif small_list:
            output_l.append(small_list)
            small_list = []
    if small_list:
        output_l.append(small_list)
    print(output_l)
    return sum([int("".join(x)) for x in output_l])


# 5. Birthday Ranges
def birthday_ranges(birthdays, ranges):
    pass