import numpy as np
from string import punctuation

LEFT_UP_SQUARE = np.array([
    ['q', 'w', 'e', 'r', 't'],
    ['a', 's', 'd', 'f', 'z'],
    ['p', 'o', 'i', 'u', 'y'],
    ['l', 'k', 'h', 'm', 'n'],
    ['x', 'c', 'v', 'b', 'g']
])
LEFT_DOWN_SQUARE = np.array([
    ['q', 'a', 'z', 'w', 's'],
    ['x', 'c', 'd', 'e', 'r'],
    ['f', 'v', 'b', 'g', 't'],
    ['y', 'h', 'n', 'm', 'u'],
    ['i', 'k', 'l', 'o', 'p']
])
RIGHT_UP_SQUARE = np.array([
    ['m', 'l', 'p', 'o', 'k'],
    ['n', 'z', 'i', 'u', 'y'],
    ['h', 'b', 'x', 'g', 'v'],
    ['t', 'f', 'c', 'd', 'r'],
    ['q', 'w', 'e', 'a', 's'],
])
RIGHT_DOWN_SQUARE = np.array([
    ['p', 'l', 'm', 'k', 'o'],
    ['i', 'n', 'u', 'h', 'b'],
    ['y', 'g', 'v', 't', 'f'],
    ['c', 'x', 'd', 'r', 'e'],
    ['w', 's', 'q', 'a', 'z'],
])


def crypt(txt, flag):
    if flag:
        key1, key2 = LEFT_UP_SQUARE, RIGHT_DOWN_SQUARE
        res1, res2 = RIGHT_UP_SQUARE, LEFT_DOWN_SQUARE
    else:
        key1, key2 = RIGHT_UP_SQUARE, LEFT_DOWN_SQUARE
        res1, res2 = LEFT_UP_SQUARE, RIGHT_DOWN_SQUARE
    lst = []
    i = 0
    while i < len(txt):
        first_key = np.where(key1 == txt[i])
        try:
            second_key = np.where(key2 == txt[i + 1])
        except IndexError:
            lst.append(txt[i])
            break

        lst.append(
            res1[first_key[0][0]][second_key[1][0]] + res2[second_key[0][0]][first_key[1][0]]
        )
        i += 2

    return ''.join(lst)


if __name__ == '__main__':
    text = open('data.txt', 'r', encoding='utf8').read()
    cp_text = ''.join(ch for ch in text.lower().replace(' ', '').replace('«', '').replace('»', '').replace('j', 'i')
                      if ch not in set(punctuation))
    crypted_text = crypt(cp_text, True)
    print("Crypted text:\n", crypted_text)
    print("Enrypted text:\n", crypt(crypted_text, False))
