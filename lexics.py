"""
find in string like this 'ABJBWLDILWUDarbsbraBWUDBUWIBDIUWBDUIDWIU' something like this 'arbsbra'
"""

income = 'ABJBWLDILWUDarbsbraBWUDBUWIBDIUWBDUIDWIUIWDI'.upper()

# variant 1
def create_main_dict(income: str, clean: bool = True) -> dict:
    """
    :param income: "abchjab
    :param clean:
    :return: {'a': [0, 5], 'b': [1, 6]}
    """
    dic = {}
    for ind, letter in enumerate(income):
        ll = dic.get(letter, [])
        ll.append(ind)
        dic[letter] = ll

    if clean:
        # delete keys with len == 1
        keys_remove = []
        for k, v in dic.items():
            if len(v) < 2:
                keys_remove.append(k)
        for i in keys_remove:
            dic.pop(i)
    return dic


def unique_sets(l: list) -> list:
    """
    :param l: list like [1, 2, 4, 5]
    :return: [{1,2}, {1,4}, {1,5}, {2,4}, {2,5}, {4,5}]
    """
    start = 1
    result = []
    for i in l[:-1]:
        for j in l[start:]:
            result.append((i, j))
        start += 1
    return result


def is_it_abcba(st: str) -> bool:
    """
    :param st: if == abcba; if == abcca
    :return: true; false
    """
    l = [i for i in st]
    l1 = l[:len(l)//2]
    if len(l) % 2 == 0:
        # even
        l2 = l[len(l)//2:]
    else:
        # odd
        l2 = l[len(l) // 2 + 1:]

    l2.reverse()
    for el1, el2 in zip(l1, l2):
        if el1 != el2:
            return False
    return True


def get_word_to_check(idx1: int, idx2: int) -> str:
    if idx2 == len(income) - 1:
        return income[idx1:]
    if idx2 < len(income) - 1:
        return income[idx1: idx2 + 1]


def main():
    last_result = ''
    dict_to_analyze = create_main_dict(income)
    for _, v in dict_to_analyze.items():
        lists_to_analyze = unique_sets(v)
        for i in lists_to_analyze:
            word = get_word_to_check(i[0], i[1])
            if is_it_abcba(word):
                if len(last_result) < len(word):
                    last_result = word
    return last_result

res = main()



# variant2

income_list = [i for i in income]
last_result = ''

def find_word(l1: list, l2: list, cental_letter= '') -> str:
    word = cental_letter
    for el1, el2 in zip(l1, l2):
        if el1 != el2:
            break
        else:
            word = el1 + word + el2
            continue
    return word


def main():
    last_result = ''
    for i, v in enumerate(income_list):
        # without letter in center
        l1 = income_list[:i]
        l2 = income_list[i:]
        l1.reverse()


        # with letter in center
        ll1 = income_list[:i]
        try:
            ll2 = income_list[i + 1:]
        except IndexError:
            break
        ll1.reverse()
        cental_letter = income_list[i]

        word1 = find_word(l1, l2)
        word2 = find_word(ll1, ll2, cental_letter)

        if len(word1) > 0:
            if len(last_result) < len(word1):
                last_result = word1

        if len(word2) > 0:
            if len(last_result) < len(word2):
                last_result = word2

    return last_result

last_result = main()


# variant 3
#  reuse is_it_abcba function

def main():
    """
    create range scanner with buffer width starting from max
    :return:
    """
    word_len = len(income)
    last_big_word = ''
    for buf_len in range(word_len, 0, -1):
        for i in range(word_len - buf_len + 1):
            start = i
            stop = buf_len + i if buf_len + i <= word_len else None
            check_sub_word = income[start:stop]
            if is_it_abcba(check_sub_word):
                if len(last_big_word) < len(check_sub_word):
                    return check_sub_word
    return last_big_word


last_result = main()