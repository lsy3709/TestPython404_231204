import bs4
import urllib.request
# 알라딘 중고서적 특정 , 
# 도서 정보를 가져오기. 콘솔 출력. 특정 한페이지만

# 함수 선언부

# <ul class="b-booklist">
    #   <li>
	#     <div class="b-cover">
    # 하위에 이미지 하나만 가져오는 테스트 
def getBookInfoImg(book_tag):
    img_tag = book_tag.find("img")
    # print(f"img_tag 결과: {img_tag}")
    img_tag_src = img_tag['src']
    
    return [img_tag_src]

# <ul class="b-booklist">
    #   <li>
	#     <div class="b-text">
    # 하위에 이미지 하나만 가져오는 테스트 
# 저자, 가격 가져오기. 
def getBookInfoTxt(book_tag):
    # 저자
    names = book_tag.find("div", {"class": "b-author"})
    authorName = names.text
    # 가격
    price = book_tag.find("div", {"class": "b-price"})
    price2 = price.find("strong")
    price3 = price2.text
    # 책 제목
    bookName = book_tag.find("a").text
    
    return [bookName,authorName, price3]

# 수정, 각각 함수를 하나로 변경. -> 보류
def getBookInfoTotal(book_tag, book_tag2):
    # 저자
    names = book_tag.find("div", {"class": "b-author"})
    authorName = names.text
    # 가격
    price = book_tag.find("div", {"class": "b-price"})
    price2 = price.find("strong")
    price3 = price2.text
    # 책 제목
    bookName = book_tag.find("a").text
    
    # 책 이미지 
    img_tag = book_tag2.find("img")
    # print(f"img_tag 결과: {img_tag}")
    img_tag_src = img_tag['src']
    
 
    return [bookName,authorName, price3,img_tag_src]


# 전역 변수부
# 해당 사이트의 하위 주소 부분 반드시 조사.
# https://www.yes24.com/24/Category/Display/001001003022?ParamSortTp=05&PageNumber=2
bookUrl = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351"

# 메인 코드부
# 가독성
htmlObject = urllib.request.urlopen(bookUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 알라딘 해당 데이터 html 모델링 계층 구조 예제
# aladinSampleTree.txt


# 태그 의 트리 구조 조사 , 정보 접근하기.
# (.) 점 : 클래스 의미, # : 아이디 의미.

tag = bsObject.find('ul', {'class': 'b-booklist'})
# 구조 일반 이미지 : <div class="b-cover">,
all_books_Img = tag.findAll('div', {'class': 'b-cover'})

# 일반 텍스트  : <div class="b-text">
all_books_Txt = tag.findAll('div', {'class': 'b-text'})

# 여기에 리스트에 해당 책의 1)a 링크 2) 이미지 주소, 
# 이미지 주소만 가져오기. 
for book in all_books_Img:
    print(getBookInfoImg(book))

# 저자, 가격 가져오기. 
for book in all_books_Txt:
    print(getBookInfoTxt(book))

# total 가져오기. 인자값을 2개로 설정을 했는데, 만들다가 잠시 보류.
# for book in all_books_Txt:
#     print(getBookInfoTotal(book))