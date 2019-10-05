import requests
for i in open('dataset_24476_3.txt'):
    i = i.rstrip()
   # print('http://numbersapi.com/{}?json'.format(i))
    res = requests.get(
        'http://numbersapi.com/{}/math?json'.format(i))# params=params)
    if res.json()['found'] == True:
        print('Interesting')
    else:
        print('Boring')

