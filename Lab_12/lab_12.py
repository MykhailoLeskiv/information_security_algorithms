from string import punctuation

ALPHABET = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м',
    'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
]


def crypt(plaintext, cipher_key, flag):
    key_as_int = [ALPHABET.index(i) for i in cipher_key]
    plaintext_int = [ALPHABET.index(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        if flag:
            value = (plaintext_int[i] + key_as_int[i]) % len(ALPHABET)
        else:
            value = (plaintext_int[i] - key_as_int[i]) % len(ALPHABET)
        ciphertext += ALPHABET[value]
    return ciphertext


if __name__ == '__main__':
    txt = open('data.txt', 'r', encoding='utf8').read()
    cp_text = ''.join(ch for ch in txt.lower().replace(' ', '') if ch not in set(punctuation))
    key = 'секрет' + cp_text
    crypted_text = crypt(cp_text, key, True)
    print("Crypted text:\n", crypted_text)
    print("Enrypted text:\n", crypt(crypted_text, key, False))
