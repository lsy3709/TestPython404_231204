import csv
import time
import datetime
# 시스템의 날짜 및 시간을  -> csv 파일 저장.

csvName = 'C:/TestPython/ch9_crawling1/datetime_231208.csv'
# 파이썬 키워드 with 시작한다, 기능 -> 파일 입출력 하기위한 객체 필요함. 
# 해당 객체를 이용 후, 자원 반납(객체 소멸)
# with 시작하면, 해당 객체를 자동으로 사용 후, 반납해줌. 
with open(csvName, 'w', newline='',encoding="UTF-8") as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초'])

count = 10
while count > 0:
    count -= 1

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')
    time_list = [yymmdd, hhmmss]
    # 출력의 형식을 2가지 표현, 1) 콘솔에 출력
    print(time_list)

    # csv 파일에 출력함.(내용을 저장하기.)
# 날짜 , 시간의 내용을 쓰는 작업. a : 추가하기.
    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(time_list)

    time.sleep(1)
