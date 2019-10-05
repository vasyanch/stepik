import sys
m = [0]
for i in range(int(input())):
    z = input()
    if 'pop' == z:
        del m[-1]
    elif 'max' == z:
        print(m[-1])
    else:
        m.append(max(int(z[5:]), m[-1]))
