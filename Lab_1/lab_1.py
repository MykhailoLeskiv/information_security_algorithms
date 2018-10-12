from string import punctuation

KEY_UKR = {
    'а': 'с', 'б': 'к', 'в': 'в', 'г': 'φ', 'ґ': 'α', 'д': '!', 'е': 't', 'є': 'χ', 'ж': 'а',
    'з': 'й', 'и': 'ω', 'і': 'о', 'ї': 'п', 'й': 'ш', 'к': 'γ', 'л': 'h', 'м': 'r', 'н': 's',
    'о': 'u', 'п': 'z', 'р': 'ї', 'с': 'ц', 'т': 'ф', 'у': 'є', 'ф': 'у', 'х': 'я', 'ц': 'л',
    'ч': 'і', 'ш': 'w', 'щ': '?', 'ь': '$', 'ю': 'β', 'я': 'ю', ' ': ' ',
}

KEY_ENG = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'I', 'i': 'p',
    'j': 'a', 'k': 's', 'l': 'd', 'm': 'f', 'n': 'g', 'o': 'h', 'p': 'j', 'r': 'k', 's': 'l',
    't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm', ' ': ' ',
}


def invert_dict(d):
    return dict([(v, k) for k, v in d.items()])


def crypt(txt, flag, filenm):
    if filenm[-3:] == 'eng':
        if flag:
            key = KEY_ENG
        else:
            key = invert_dict(KEY_ENG)
    else:
        if flag:
            key = KEY_UKR
        else:
            key = invert_dict(KEY_UKR)

    lst = []
    if flag:
        s = ''.join(ch for ch in txt if ch not in set(punctuation))
        s = s.lower()
    else:
        s = ''.join(ch for ch in txt)

    for ch in s:
        lst.append(key[ch])
    return ''.join(lst)


if __name__ == '__main__':
    filename = input('Enter name of file: ')
    try:
        f = open(filename + '.txt', 'r', encoding='utf-8-sig')
    except FileNotFoundError:
        print('Cannot find file!')
        exit(-1)
    else:
        text = crypt(f.read(), True, filename)
        print('Crypted text:\n', text)
        print('Encrypted text:\n', crypt(text, False, filename))
