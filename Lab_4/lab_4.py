from itertools import cycle


def encode(xs, height):
    xs = xs.replace(' ', '')
    positions = pattern(height, len(xs))
    return ''.join(xs[i] for _, i in positions)


def decode(xs, height):
    positions = pattern(height, len(xs))
    rectified = sorted(enumerate(positions), key=lambda t: t[1][1])
    return ''.join(xs[i] for i, _ in rectified)


def pattern(height, width):
    n = 2 * (height - 1)
    positions = (min(x, n - x) for x in cycle(range(n)))
    return sorted(zip(positions, range(width)))


if __name__ == '__main__':
    text = open('data.txt', 'r', encoding='utf8').read()

    layers = int(input('Enter number of layers: '))
    crypted_text = encode(text, layers)
    print('Crypted text: ', crypted_text)
    print('Encrypted text: ', decode(crypted_text, layers))
