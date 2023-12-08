import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox
import re
# 주의사항, 문자열 안에 특수문자 부분 체크 잘하기.

# 현재 네이트 기사는 특정 시간 예 1분마다 새로운 기사가 나옴.

# 그래서, 현재 페이지에 1페이지에서 20개 기사만 디비에 저장하기로 함.

# 특정 시간 time.sleep(300), 5분정도 인터벌을 두고 저장하기로 함.

# 예스24는 한페이지의 상품이 고정,
# 뉴스는 실시간으로 계속 생성됨.

# 아래 코드, 웹 상에 접근시, 인증 된 여부를 확인시 필요한 부분,
# ssl 설정을 none 했음.
# 맥북 테스트, 아래 오류가 발생해서, 임시 방편으로 처리한 코드임.
ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

# 전역변수, 기사에서 가지고 올 정보만 선택한 변수.
imgLinkUrl, subject, link, press, pDate, pTime = "", "", "", "", "", ""
# null = None
# 함수 선언 부분

# regex 이용해서, re.sub(매개변수1,매개변수2,매개변수3)
# 매개변수1 : 특정 조건
# 매개변수2 : 대체할 문자
# 매개변수3 : regex를 적용할 문장.


def clean_text(inputString):
    text_rmv = re.sub(
        '[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', inputString)
    return text_rmv

# 가져올 정보를 , pymysql를 이용해서, 실제로 추가하는 부분.


def insertData(subject, press, pDate, pTime, link, imgLinkUrl):
    # con : 파이썬 <-> mysql 연결하기 위한 인스턴스, 도구
    # cur : 디비의 정보를 조작하기위한 도구.
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4, data5, data6 = "", "", "", "", "", "", ""
    sql = ""
    con = pymysql.connect(host='127.0.0.1', user='root',
                          password='1234', database='nateNewsLive', charset='utf8')
    cur = con.cursor()
#    title` VARCHAR(200) NULL,
#   `publisher` VARCHAR(45) NULL,
#   `newsDate` VARCHAR(10) NULL,
#   `newsTime` VARCHAR(6) NULL,
#   `newsDetail` VARCHAR(200) NULL,
#   `newsImgUrl` VARCHAR(200) NULL,
    # data0 = data10
    data1 = subject
    data2 = press
    data3 = pDate
    data4 = pTime
    data5 = link
    data6 = imgLinkUrl
    # data1 = clean_text(subject)
    # data2 = clean_text(press)
    # data3 = clean_text(pDate)
    # data4 = clean_text(pTime)
    # data5 = clean_text(link)
    # data6 = clean_text(imgLinkUrl)
    #
    try:
        # print(null)
        # print("데이터 실행전 확인")
        # print(data1)
        # print(data2)
        # print(data3)
        # print(data4)
        # print(data5)
        # print(data6)
        # query = "INSERT INTO newsTable (title, publisher, newsDate, newsTime, newsDetail, newsImgUrl) VALUES (?, ?, ?, ?, ?, ?)"
        # values = (data1, data2, data3, data4, data5, data6)
        sql = "INSERT INTO newsTable (title,publisher,newsDate,newsTime,newsDetail,newsImgUrl)  VALUES('" + \
            data1 + "','" + data2 + "','" + data3 + "','" + \
            data4 + "','" + data5 + "','"+data6 + "')"
        print("순서2 : sql 실행전 ")
        print(f"sql : {sql}")

        cur.execute(sql)

        # cur.execute(query, values)
    except:
        print('================================')
        print("순서3 : 예외 발생")
        print('================================')
        # messagebox.showerror('오류', '데이터 입력 오류가 발생함')
    else:
        print('================================')
        print("순서3: 성공")
        print('================================')
        # messagebox.showinfo('성공', '데이터 입력 성공')
    con.commit()
    con.close()


##
page = 1
count = 1
nateUrl = "https://news.nate.com/recent?cate=its&mid=n0105&type=c&date=20230829&page=1"
while True:
    # if (count != 21):
    try:
        newsUrl = nateUrl + str(page)
        newsUrl = nateUrl
        page += 1
        htmlObject = urllib.request.urlopen(newsUrl, context=ssl_context)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        tag_list = bsObject.findAll('div', {'class': 'mlt01'})
        print('###### 실시간 뉴스 속보 #######')
        for tag in tag_list:
            # if (count != 21):
            # strong -> h2 변경 230629 (확인 날짜)
            subject = tag.find('h2', {'class': 'tit'}).text
            subject = clean_text(subject)
            link = tag.find('a', {'class': 'lt1'})['href']
            link = 'https:' + link
            imgLink = tag.find('em', {'class': 'mediatype'})
            # 이미지 없는 경우 처리 부분. 파이썬 null 대신  None
            if imgLink != None:
                imgLinkUrl = imgLink.find('img')['src']
                imgLinkUrl = 'https:' + imgLinkUrl
            else:
                imgLinkUrl = '이미지가 존재 하지 않음'
            pressAndDate = tag.find('span', {'class': 'medium'}).text
            pressAndDate.replace('\t', ' ')
            pressAndDate.replace('\n', '')
            if len(pressAndDate.split()) == 3:
                press, pDate, pTime = pressAndDate.split()
            elif len(pressAndDate.split()) == 4:
                press1, press2, pDate, pTime = pressAndDate.split()
                press = press1+press2
            else:
                pTime = 'pTime없음'
                pDate = 'pDate없음'
                press = 'press없음'
                # continue
            print("순서1: 데이터 추가 전")
            print("subject: %s" % (subject))
            print("press: %s" % (press))
            print("pDate: %s" % (pDate))
            print("pTime: %s" % (pTime))
            print("link: %s" % (link))
            print("imgLinkUrl: %s" % (imgLinkUrl))
            print("count : %d" % count)
            print('================================')
            print('================================')
            insertData(subject, press, pDate, pTime, link, imgLinkUrl)
            count += 1
            # print('(' , page, ')', subject)
            # print('\t https:'+link, press, pDate, pTime)
            # print('\t imgLink : '+ imgLinkUrl)
        time.sleep(10)
    except:
        break
    # else:
    #     break
    # 특정 시간마다 동작 여부
        # time.sleep(60)
