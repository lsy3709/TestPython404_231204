import bs4
import urllib.request
import csv

# 알라딘  -> csv

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



# 전역 변수부
# url = "http://www.yes24.com/24/Category/Display/001001003022004?ParamSortTp=05&PageNumber="
# pageNumber = 1

# 전역 변수부
# 해당 사이트의 하위 주소 부분 반드시 조사.
# https://www.yes24.com/24/Category/Display/001001003022?ParamSortTp=05&PageNumber=2
url = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351"


# 전체 리스트 
result_list = []

# 메인 코드부
csvName = 'C:/TestPython/ch9_crawling1/aladinBook_231208.csv'
with open(csvName, 'w', newline='',encoding="UTF-8") as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['책이름', '저자', '가격', '책커버이미지'])

while True:
    try:
        # 초기세팅
        htmlObject = urllib.request.urlopen(url)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')


        tag = bsObject.find('ul', {'class': 'b-booklist'})
        # 구조 일반 이미지 : <div class="b-cover">,
        all_books_Img = tag.findAll('div', {'class': 'b-cover'})

        # 일반 텍스트  : <div class="b-text">
        all_books_Txt = tag.findAll('div', {'class': 'b-text'})

        # 이미지 주소만 가져오기. 
        for book in all_books_Img:
            bookImg = getBookInfoImg(book)
            bookImgTxt = bookImg[0]
            result_list.append(bookImgTxt)

        # 저자, 가격 가져오기. 
        for book in all_books_Txt:
            bookTxt = getBookInfoTxt(book)
            bookName = bookTxt[0]
            result_list.append(bookName)
            bookAuthor = bookTxt[1]
            result_list.append(bookAuthor)
            bookPrice = bookTxt[2]
            result_list.append(bookPrice)

        # for book in result_list:
        #     info_list = getBookInfo(book)
        print(f"result_list : {result_list}")
        with open(csvName, 'a', newline='',encoding="UTF-8") as csvFp:
            csvWriter = csv.writer(csvFp)
            csvWriter.writerow(result_list)

    except:
        break

print('Save. OK~')
