def merge(intervals):
    # print(intervals)
    # print(type(intervals))
    sorted_arr = intervals.sort() # [[1,3],[2,6],[8,10],[15,18]]
    print(type(sorted_arr))
    merged = [intervals[0]]
    # print('merged at 0', merged)

    for current in intervals[1:]:
        print(current)
        if current[0] <= merged[-1][1]:
            print(merged[-1][1])
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)

    return merged

# print(merge([[1,3],[2,6],[8,10],[15,18]]))


def get_intervals(intervals):
    intervals.sort()
    last = [intervals[0]]
    # print(result)

    for list_item in intervals[1:]:
        if list_item[0] <= last[-1][1]:
            last[-1][1] = max(last[-1][1], list_item[0])
        else:
            last.append(list_item)

    return last


# print(get_intervals([[1,3],[2,6],[8,10],[15,18]]))

## count word occurence

sentence = "I love python and i love ai in python"

def count_occurence_max(sentence:str):
    words = sentence.lower().split()
    # print(words)
    check = {}
    for word in words:
        # print(word)
        check[word] = sentence.count(word)

    return check

# print(count_occurence_max(sentence))

def count_occurence(sentence:str):
    words = sentence.lower().split()
    # print(words)
    check = {}
    for word in words:
        if word in check:
            check[word] += 1
        else:
            check[word] = 1

    return check

# print(count_occurence(sentence))

# --------  remove vowels ----
text = "Artificial Intelligence"

def remove_vowels(text: str):
    vowels = 'aeiouAEIOU'
    result = ''
    # text = text.lower()
    for char in text:
        if char not in vowels:
            result += char

    return result

# print(remove_vowels(text))

# ---- Characters Appearing Only Once -------

s = "i love python"

def check_only_once(s: str):
    result = ''

    for char in s:
        count = 0
        for item in s:
            if char == item:
                count += 1

        if count == 1:
            result += char

    return result

# print(check_only_once(s))


# ------------------------- matrix transpose -----------------
matrix = [
    [1,2],
    [4,5]
]

def matrix_transpose(current_matrix):

    rows = len(current_matrix)
    cols = len(current_matrix[0])
    transpose = []


    for col in range(cols):
        row = []

        for r in range(rows):
            row.append(matrix[r][col])

        transpose.append(row)

    return transpose

print(matrix_transpose(matrix))