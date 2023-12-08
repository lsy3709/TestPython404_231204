import bs4

webPage = open('C:/CookAnalysis/HTML/Sample02.html',
               'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

#
tag_ul = bsObject.find('ul')
print(tag_ul)
print()

tag_li = bsObject.find('li')
print(tag_li)
print()

# 복수개를 찾아서 , 리스트에 담아서 작업.
tag_li_all = bsObject.findAll('li')
print(tag_li_all)
