'''
алгоритм Рабина-Карпа
'''
import sys


def hash_fun(s, x, p):
    has = 0
    xi = 1
    for v in s:
        has = (has + ord(v) * xi) % p
        ans = xi
        xi = (xi * x) % p
    return has, ans


def substring(pattern, string, x, p):
    lp = len(pattern)
    lt = len(string)
    ans = ''
    hpat = hash_fun(pattern, x, p)
    hp, h0 = hpat[0], hpat[1]
    h = hash_fun(string[lt - lp:], x, p)[0]
    #print(h0)
    if h == hp and string[lt - lp] == pattern[0] and string[lt - 1] == pattern[lp - 1]:
        ans = ' ' + str(lt - lp) + ans
    i = lt - lp - 1
    while i > -1:
        h = (((h - ord(string[i + lp]) * h0) * x) + ord(string[i])) % p
        h = (h + p) % p
        if h == hp and string[i] == pattern[0] and string[i + lp - 1] == pattern[-1]:
            ans = ' ' + str(i) + ans
        i -= 1
    return ans


if __name__ == '__main__':
    pattern_ = sys.stdin.readline().strip()
    string = sys.stdin.readline().strip()
    #print(pattern_, string)
    p_ = 1000000007
    x_ = 15
    print(substring(pattern_, string, x_, p_))
