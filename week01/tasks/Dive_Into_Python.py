
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


# read data from cli
def read_input():
    word = input()
    size = input().split()
    size[0] = int(size[0])
    size[1] = int(size[1])
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
    diagonals = []
    max_row = len(matrix)
    max_col = len(matrix[0])

    # get main diagonal and above it
    for col in range(0, max_col):
        r = 0
        c = col
        d = []
        while r < max_row and c < max_col:
            d.append(matrix[r][c])
            r += 1
            c += 1
        diagonals.append(d)

    # get diagonals below main diagonal
    for row in range(1, max_row):
        r = row
        c = 0
        d = []
        while r < max_row and c < max_col:
            d.append(matrix[r][c])
            r += 1
            c += 1
        diagonals.append(d)

    # get second main diagonal and above it
    for col in range(max_col - 1, -1, -1):
        r = 0
        c = col
        d = []
        while r < max_row and c >= 0:
            d.append(matrix[r][c])
            r += 1
            c -= 1
        diagonals.append(d)

    # get second diagonals below main diagonal
    for row in range(1, max_row):
        r = row
        c = max_col - 1
        d = []
        while r < max_row and c >= 0:
            d.append(matrix[r][c])
            r += 1
            c -= 1
        diagonals.append(d)

    return diagonals


# get matrix columns (transpose matrix)
def columns(m):
    t_m = []
    for c in range(len(m[0])):
        t_m.append([row[c] for row in m])
    return t_m


# check if name is palindrome Palindrome
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


#
def word_counter():
    word, size, matrix = read_input()
    if len(matrix) != size[0] or len(matrix[0]) != size[1]:
        print('Invalid number of rows or columns!')
        return 0

    suma = count_words_in_ll(matrix,word)  # rows
    suma += count_words_in_ll(reversed_rows(matrix),word)  # reversed rows
    suma += count_words_in_ll(columns(matrix), word)  # columns
    suma += count_words_in_ll(reversed_rows(columns(matrix)), word) # reversed columns
    suma += count_words_in_ll(find_diagonals(matrix),word)  # diagonals
    suma += count_words_in_ll(reversed_rows(find_diagonals(matrix)), word)  # reversed diagonals

    if palindrome(word):
        return suma//2
    else:
        return suma


# -------------------------------------------------------------------------

# Gas Stations

