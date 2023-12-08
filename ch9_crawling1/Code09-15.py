import bs4
import urllib.request
# yse24 특정 , 도서 정보를 가져오기. 콘솔 출력. 페이지 끝까지

# 함수 선언부


def getBookInfo(book_tag):
    # 각 정보, 저자, 발행일, 출판사, 가격 등 추출.하는 작업.
    # div: .goods_name
    names = book_tag.find("div", {"class": "goods_name"})
    # div: .goods_name -> a 태그의 text 속성 값 조회.
    bookName = names.find("a").text

    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text

    bookPub = book_tag.find("span", {"class": "goods_pub"}).text
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    return [bookName, bookAuth, bookPub, bookDate, bookPrice]


# 전역 변수부
url = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber="
pageNumber = 1

# 메인 코드부
while True:
    try:
        # 페이지 끝까지 가게되면, 이제 반복문 종료 하게끔.
        # try , 오류가 발생해도 예외처리를 하니, 비정상 종료를 막음.
        # url 기본 주소에, 해당 페이지 번호만 , 문자열로 변환해서 , 추가.
        bookUrl = url + str(pageNumber)
        pageNumber += 1

        # 가독성,
        htmlObject = urllib.request.urlopen(bookUrl)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        # 특정 카테고리 -> 판매량 -> 해당 도서 정보 리스트를 추출.
        tag = bsObject.find('ul', {'class': 'clearfix'})
        all_books = tag.findAll('div', {'class': 'goods_info'})

        # all_books , 같은 포맷형식으로 된 책들의 정보를 담은 리스트.
        # all_books<bookModel>
        for book in all_books:
            # 같은 구조의 형식이니, 함수로 리팩토링해서, 정보를 추출.
            print(getBookInfo(book))

    except:
        break
