'''
    Данный код реализует кодирование Хаффмана строки
    состоящей из латинских строчнных букв размером <= 10^4 символов.
    В первой строке программа выводит количество различных букв k,
    встречающихся в строке и размер получившейся закодированной строки.
    В следующих k строках выводятся коды букв в формате "letter: code".
    В последней строке пишется закодированная строка.
'''

import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    h = []
    for char, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(char)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, a, left = heapq.heappop(h)
        freq2, a_, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        (_freq, _a, root) = h[0]
        root.walk(code, '')
    return code


def main():
    s = input('')
    code = huffman_encode(s)
    encode = ''.join(code[ch] for ch in s)
    print(len(code), len(encode))
    for ch in code:
        print('{0}: {1}'.format(ch, code[ch]))
    print(encode)

if __name__ == '__main__':
    main()