from urllib import request

responce = request.urlopen("http://example.com")

html = responce.read().decode()

html_str = str(html)
start = html_str.find('<title>')
end = html_str.find('</title>')

char_count = len('<title>')
print('Content: ', html_str[start+char_count:end])

