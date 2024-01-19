# 모듈을 불러오기
import requests
#API URL을 사전에 정의
url = "https://open.jejudatahub.net/api/proxy/5D5a577taba7tbb71at1b1bt9tatata9/tpbbtt52jppbe3rt3c_e3tp2cb252ctb?startDate=20180101&endDate=20181231&cityGubun=읍면&marketType=유흥&userType=내국인관광객&ageGroup=20대&gender=여&sigungu=제주시"

#임포트한 모듈을 통해 get방식 요청을 보냄. 응답 객체를 response 변수에 저장
response = requests.get(url)
#json을 읽을 수 있도록 응답객체를 json으로 전환
data = response.json()
print(data)