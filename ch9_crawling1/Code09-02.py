import urllib.request
# pip install bs4 , 설치 필요.
import bs4

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
# 위에 코드는 정리가 덜된 태그 집합
# 아래 코드는 bs4-> BeautifulSoup 클래스를 이용해서, 가독성있게 변환.
bsObject = bs4.BeautifulSoup(htmlObject, 'html.parser')

# 결론, 변환을 해주는 BeautifulSoup 을 이용해서 작업한다.
print(bsObject)
