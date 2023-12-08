import bs4

#초기세팅
webPage = open('C:/TestPython/ch9_crawling1/Sample03.html',
               'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')


ul_value = bsObject.find('ul', {'class': 'myClass2'})
print(ul_value)

li_list = bsObject.findAll('li', {'class': 'myClass3'})
print(li_list)
