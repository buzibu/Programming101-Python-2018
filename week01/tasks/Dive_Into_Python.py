
# Counting substrings
def count_substrings(haystack, needle):
    c = 0
    if len(haystack) >= len(needle):
        go_on = 0
        for i in range(len(haystack) - len(needle) + 1):
            if go_on == 0:
                if needle == haystack[i:i + len(needle)]:
                    c += 1
                    go_on = len(needle) - 1
            else:
                go_on -= 1
    return c


# Sum Numbers in Matrix
def sum_matrix(m):
    s = 0
    for i in m:
        for j in i:
            s += j
    return s


# NaN Expand
def nan_expand(times):
    if times == 0:
        return ''
    else:
        return ('Not a '*times) + 'NaN'


# Integer prime factorization
def prime_factorization(n):
    pass


# The group function
def group(li):
    big_list = []
    g = 0
    for i, ch in enumerate(li):
        if i == 0:
            big_list.append([ch])
        else:
            if ch == li[i - 1]:
                big_list[g].append(ch)
            else:
                g += 1
                big_list.append([ch])
    return big_list


# Longest subsequence of equal consecutive elements
def max_consecutive(items):
    maximum = 0
    for x in group(items):
        if len(x)> maximum:
            maximum = len(x)
    return maximum


# Word counter
# -------------------------------------------------------------------------
# count words in list of lists
def count_words_in_ll(mat,word):
    c = 0
    for row in mat:
         c += count_substrings(''.join(row),word)
    return c

def read_input():
    word = input()
    size = input().split()
    matrix = []
    while True:
        line = input()
        if line == '':
            break
        else:
            matrix.append(list(line.replace("\t", "").replace(" ", "")))
    print(word)
    print(size)
    print(matrix)
    return word, size, matrix


# reverse matrix rows
def reversed_rows(matrix):
    reversed_matrix = []
    for row in matrix:
        reversed_matrix.append(row[::-1])
    return reversed_matrix


# return list of matrix diagonals
def find_diagonals(matrix):

    pass


def word_counter():
    word, size, matrix = read_input()
    suma = count_words_in_ll(matrix,word)
    suma += count_words_in_ll(reversed_rows(matrix),word)
    suma += count_words_in_ll(reversed_rows(matrix), word)
    suma += count_words_in_ll(find_diagonals(matrix),word)
    suma += count_words_in_ll(reversed_rows(find_diagonals(matrix)), word)
    return suma

# -------------------------------------------------------------------------
