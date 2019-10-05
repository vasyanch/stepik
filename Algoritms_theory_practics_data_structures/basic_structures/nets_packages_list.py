#-*-coding:utf8;-*-
#qpy:3
#qpy:console


def do(size, n):
    q = []
    for i in range(n):
        arr, dur = map(int, input().split())
        while q and arr >= q[0]:
            del q[0]
        if len(q) < size:
            if not q:
                ch =arr 
            print(ch)
            ch = ch + dur 
            q.append(ch)
        else:
            print(-1)

if __name__ == '__main__':
    size_, n_ = list(map(int, input().split()))
    do(size_, n_)