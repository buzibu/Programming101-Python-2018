# Sum of all digits of a number

def sum_of_digits(n):
    return sum([int(x) for x in list(str(abs(n)))])


# Turn a number into a list of digits

def to_digits(n):
    return [int(x) for x in list(str(n))]


# Turn a list of digits into a number

def to_number(digits):
    return int(''.join([str(x) for x in digits]))


# Factorial Digits

def fact_digits(n):
    import math
    return sum([math.factorial(int(x)) for x in list(str(n))])


# First nth members of Fibonacci

def fibonacci(n):
    n = abs(n)
    def fib(x):
        if x == 0:
            return 1
        elif x == 1:
            return 1
        else:
            return fib(x - 1) + fib(x - 2)
    return [fib(a) for a in range(0,n)]


# Fibonacci number

def fib_number(n):
    n = abs(n)

    def fib(x):
        if x == 0:
            return 1
        elif x == 1:
            return 1
        else:
            return fib(x - 1) + fib(x - 2)

    return int(''.join([str(fib(a)) for a in range(0,n)]))


# Palindrome

def palindrome(n):
    nstr = str(n)
    first_part = nstr[:len(nstr)//2]
    if len(nstr)%2 == 0:
        second_part = nstr[-len(nstr)//2:]
    else:
        second_part = nstr[-(len(nstr)-1)//2:]
    if first_part == second_part[::-1]:
        return True
    else:
        return False


# Vowels in a string

def count_vowels(str):
    vowels = set('aeiouy')
    cnt = 0
    for i in str.lower():
        if i in vowels:
            cnt += 1
    return cnt


# Consonants in a string

def count_consonants(str):
    cons = set('bcdfghjklmnpqrstvwxz')
    cnt = 0
    for i in str.lower():
        if i in cons:
            cnt += 1
    return cnt


# Char Histogram

def char_histogram(string):
    c_dict = {}
    for key in string:
        if key in c_dict:
            c_dict[key] += 1
        else:
            c_dict[key] = 1
    return c_dict

