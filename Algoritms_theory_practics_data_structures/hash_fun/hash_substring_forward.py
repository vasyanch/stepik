import sys


def hash_fun(s, x, p):
    has = 0
    for i, v in enumerate(s):
        xi = pow(x, i, p)
        has = (has % p + (ord(v) * xi) % p) % p
        # ans = xi
        # xi = (xi * x) % p
    return has, xi


pattern = sys.stdin.readline().strip()
string = sys.stdin.readline().strip()
#print(pattern_, string)
p = 1000000007
x = 15
lp = len(pattern)
lt = len(string)
ans = ''
hpat = hash_fun(pattern, x, p)
hp, h0 = hpat[0], hpat[1]
h = hash_fun(string[lt - lp:], x, p)[0]
#print(h0)
if h == hp and string[lt - lp] == pattern[0] and string[lt - 1] == pattern[lp - 1]:
    ans = ' ' + str(lt - lp) + ans
for i in range(lt - lp - 1, -1, -1):
    h = (((h - ord(string[i + lp]) * h0) * x) + ord(string[i])) % p
    if h == hp and string[i] == pattern[0] and string[i + lp - 1] == pattern[-1]:
        ans = ' ' + str(i) + ans
print(ans)
