# мультиплексирование

readsocks, writesocks = [...], [...] # сокеты
while True:
    readables, writeables, exeptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        data = sockobj.recv(512)
        if not data:
            sockobj.close()
            readsocks.remove(sockobj)
        else:
            print('\tgot', data, 'on', id(sockobj))
`
