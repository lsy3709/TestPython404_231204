import bs4
import urllib.request

nateUrl = "https://news.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div : 속성:class, 값: snbArea ->
tag = bsObject.find('div', {'class': 'snbArea'})

print('## 네이트 뉴스의 메뉴 목록 ##')
# div : 속성:class, 값: snbArea -> li 태그를 모두 찾아서 리스트에 담기
# li_list
li_list = tag.findAll('li')
for li in li_list:
    # 하나씩 꺼내서, 텍스트 속성만 출력.
    print(li.text, end='  ')
    print(f"li 의 내용 : {li}")
    a_tag = li.find("a")
    print(f"a_tag 결과: {a_tag}")
    a_tag_href = a_tag['href']
    print(f"a_tag_href 결과: {a_tag_href}")
    # print(li['href'], end='  ')
