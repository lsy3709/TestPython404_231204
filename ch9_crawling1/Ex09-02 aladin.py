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
    names = book_tag.find("div", {"class": "b-author"})
    authorName = names.text
    price = book_tag.find("div", {"class": "b-price"})
    price2 = price.find("strong")
    price3 = price2.text
    
 
    return [authorName, price3]


# 전역 변수부
# url = "http://www.yes24.com/24/Category/Display/001001003022004?ParamSortTp=05&PageNumber="
# pageNumber = 1

# 전역 변수부
# 해당 사이트의 하위 주소 부분 반드시 조사.
# https://www.yes24.com/24/Category/Display/001001003022?ParamSortTp=05&PageNumber=2
url = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351"


# 메인 코드부
csvName = 'C:/TestPython/ch9_crawling1/aladinBook_231208.csv'
with open(csvName, 'w', newline='',encoding="UTF-8") as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['책이름', '저자', '출판사', '출간일', '가격'])

while True:
    try:
        bookUrl = url + str(pageNumber)
        pageNumber += 1

        htmlObject = urllib.request.urlopen(bookUrl)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        tag = bsObject.find('ul', {'class': 'clearfix'})
        all_books = tag.findAll('div', {'class': 'goods_info'})

        for book in all_books:
            info_list = getBookInfo(book)
            with open(csvName, 'a', newline='') as csvFp:
                csvWriter = csv.writer(csvFp)
                csvWriter.writerow(info_list)

    except:
        break

print('Save. OK~')
