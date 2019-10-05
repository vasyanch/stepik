'''
Задача: поверить корректность растановки скобок в строке.
Вход: строка
Выход: индекс первой некорректной скобки или Success
       если все верно.
'''


def brackets(_string):
    a = []
    br = {')': '(', ']': '[', '}': '{'}
    for i, v in enumerate(_string, start=1):
        if v in br.values():
            a.append((v, i))
        if v in br:
            if not a or a.pop()[0] != br[v]:
                return i
    return a[-1][1] if a else 'Success'


if __name__ == '__main__':
    s = input()
    print(brackets(s))