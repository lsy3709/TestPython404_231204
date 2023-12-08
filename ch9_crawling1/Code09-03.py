import bs4
# 실제 사이트에 접근하기 전에,
# 임시 html에서, 각 태그별 접근 연습.
webPage = open('C:/CookAnalysis/HTML/Sample02.html',
               'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

print(bsObject)
