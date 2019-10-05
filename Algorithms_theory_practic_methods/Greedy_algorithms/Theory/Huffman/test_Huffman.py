import random, string
from Huffman_decode import huffman_decode
from Huffman_encode import huffman_encode, Node, Leaf


def test(n):
    for i in range(n):
        len_ = random.randint(0, 32)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(len_))
        print(s)
        code = huffman_encode(s)
        assert s == huffman_decode(''.join(code[ch] for ch in s), code)
    return ('Exellent!')



if __name__ == '__main__':
    print(test(1))
