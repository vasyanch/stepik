import urllib

url = 'http://api.site.com/method/'
values = {'argument': 'value', 'argument2': 'value2'}

headers = {'User-Agent': 'python urllib2'}
data = urllib.urlencode(values)
req = urllib.Request(url, data, headers)
response = urllib.urlopen(req)
result = respose.read()
