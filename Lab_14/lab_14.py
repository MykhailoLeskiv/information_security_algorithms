def crypt(txt, key):
    lst = [[] for _ in range(len(key))]
    j = 0
    for i in txt:
        lst[j].append(i)
        if j < len(key) - 1:
            j += 1
        else:
            j = 0

    lst = [x for _, x in sorted(zip(key, lst))]

    united_lst = []
    for i in lst:
        for j in i:
            united_lst.append(j)

    return ''.join(united_lst)


def encrypt(txt, key):
    remainder = len(txt) % len(key)
    snippet_len = int(len(txt) / len(key))
    key_lst = [key.index(i) for i in sorted(key)]
    lst = []
    i = 0
    iter_index = 0
    while i < len(txt):
        if key_lst[iter_index] < remainder:
            lst.append([i for i in txt[i:i + snippet_len + 1]])
            i = i + snippet_len + 1
        else:
            lst.append([i for i in txt[i:i + snippet_len]])
            i = i + snippet_len
        iter_index += 1
    lst = [x for _, x in sorted(zip(key_lst, lst))]
    united_lst = []
    for i in range(snippet_len + 1):
        for j in lst:
            try:
                united_lst.append(j[i])
            except IndexError:
                pass
    return ''.join(united_lst)


if __name__ == '__main__':
    text = open('data.txt', 'r', encoding='utf8').read()
    key = 'секрeт'
    crypted_text = crypt(text, key)
    print("Crypted text:\n", crypted_text)
    print("Enrypted text:\n", encrypt(crypted_text, key))
