import bs4

# 해당, url, 특정 html 문서이건 접근하기위한 초기 세팅. 
webPage = open('C:/TestPython/ch9_crawling1/Sample02.html',
               'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 특정 태그를 찾는 연습.
# 실제로 수집 하고 싶은 특정 태그의 정보를 찾는 연습. 
tag_div = bsObject.find('div')
print(tag_div)
