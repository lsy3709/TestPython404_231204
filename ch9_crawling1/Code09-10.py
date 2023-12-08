import bs4
import urllib.request

# 찾을 때, 웹 브라우저의 검사 (f12 개발자 도구 , element 요소탭에서)
# ctrl + shift + c, 웹 화면에 마우스 커서를 올려보면 해당 요소의 태그및
# 정보를 알수 있음. 그러면, 그정보를 가지고 크롤링을 함.
# 크롤링을 하기 위한 준비물. -> 찾아서 정리하는 시간이 오래 걸림.

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
# 가독성 있게 다 변환을 한 상태.
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div-> id 속성 값:NateBi , 네이트 로고
tag = bsObject.find('div', {'id': 'NateBi'})
print(tag, '\n')

# div -> id 속성 값:NateBi : tag 담았고 ->하위에 a 태그 찾기 : a_tag
a_tag = tag.find("a")
print(a_tag, '\n')

# div -> id 속성 값:NateBi : tag 담았고 ->하위에 a 태그 찾기 : a_tag
# 이어서 속성 href 의 값만 추출.
href = a_tag['href']
print(href, '\n')

# div -> id 속성 값:NateBi : tag 담았고 ->하위에 a 태그 찾기 : a_tag
# text 만 가져오기.
text = a_tag.text
print(text)
