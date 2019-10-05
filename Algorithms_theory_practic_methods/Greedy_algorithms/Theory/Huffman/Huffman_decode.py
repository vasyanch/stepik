'''
     Данный код реализует декодирование строки закодированной по алгоритму Хаффмана.
     В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв,
     встречающихся в строке, и размер получившейся закодированной строки, соответственно.
     В следующих k строках записаны коды букв в формате "letter: code".
     В последней строке записана закодированная строка.
     Программа выводи строку s, состоящую из латинских букв и соответствующую заданому двоичному
     коду на входе.
'''


def main():
    num_dif, len_code = map(int,input('').split())
    codes = {}
    for i in range(num_dif):
        l = list(map(str.strip, input('').split(':')))
        codes[l[0]] = l[1]
    return huffman_decode(input(), codes)


def huffman_decode(s, codes, decode='', a=''):
    code = {}
    for i in codes.items():
        code[i[1]] = i[0]
    for i in  s:
        a += i
        if a in code:
            decode += code[a]
            a = ''
    return decode

if __name__ == '__main__':
    print(main())