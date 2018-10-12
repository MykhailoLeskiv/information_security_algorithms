from string import punctuation
from random import randint

KEY_UKR = {
    'а': ('14', '16', '75', '44', '19', '71', '10'), 'б': ('72',),
    'в': ('11', '77', '15', '29', '34'), 'г': ('18',), 'ґ': ('00',), 'д': ('02', '55', '17'),
    'е': ('12', '13', '79', '61'), 'є': ('01',), 'ж': ('03',), 'з': ('99', '05'),
    'и': ('54', '41', '68', '93', '37'), 'і': ('22', '63', '87'), 'ї': ('46',), 'й': ('80',),
    'к': ('85', '48', '33'), 'л': ('52', '74', '66'), 'м': ('57', '42'),
    'н': ('20', '50', '39', '82', '90', '84', '96'),
    'о': ('26', '08', '92', '91', '38', '45', '67', '32'), 'п': ('94', '25'),
    'р': ('62', '27', '76', '60'), 'с': ('09', '95', '53'), 'т': ('21', '43', '65', '98', '86'),
    'у': ('31', '64', '97'), 'ф': ('73',), 'х': ('88',), 'ц': ('23',), 'ч': ('81',), 'ш': ('59',),
    'щ': ('06',), 'ь': ('28', '36'), 'ю': ('40',), 'я': ('58', '24'),
    ' ': ('04', '07', '83', '30', '35', '47', '49', '51', '56', '89', '69', '70', '78'),
}

KEY_ENG = {
    'a': ('07', '14', '33', '45', '62', '91'), 'b': ('17', '23', '55', '73'),
    'c': ('04', '20', '31', '76'), 'd': ('12', '49', '60', '71'),
    'e': ('01', '27', '84', '54', '81', '90'), 'f': ('40', '51', '65', '80', '94'),
    'g': ('08', '21', '77'), 'h': ('35', '99'), 'i': ('02', '13', '41', '57', '78'),
    'j': ('22', '61', '86'), 'k': ('15', '88'), 'l': ('05', '37', '42', '70', '97'),
    'm': ('18', '24', '56', '82'), 'n': ('06', '44', '92'),
    'o': ('09', '11', '30', '46', '79', '96'), 'p': ('25', '36', '47', '59'),
    'r': ('03', '58', '67', '72'), 's': ('43', '74', '98'),
    't': ('10', '29', '64'), 'u': ('59', '75', '95'), 'v': ('16', '63', '85'),
    'w': ('26', '52'), 'x': ('39', '50'), 'y': ('28', '48'), 'z': ('68', '89'),
    ' ': ('19', '32', '34', '38', '53', '66', '69', '83', '87', '93'),
}


def invert_dict(d):
    lst = []
    for k, v in d.items():
        for e in v:
            lst.append((e, k))
    return dict(lst)


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

    if flag:
        for ch in s:
            lst.append(key[ch][randint(0, len(key[ch]) - 1)])
    else:
        ch = 0
        while ch < len(s):
            lst.append(key[s[ch:ch + 2]])
            ch += 2
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