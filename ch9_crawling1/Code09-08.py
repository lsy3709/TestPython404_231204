import bs4

#초기세팅
webPage = open('C:/TestPython/ch9_crawling1/Sample03.html',
               'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 간단하지만, 중요함. 활용도가 높음.
a_list = bsObject.findAll('a')
print(f"a_list 의 결과 : {a_list}")

# 매우 많이 사용 됨.
for aTag in a_list:
    print(aTag['href'])
