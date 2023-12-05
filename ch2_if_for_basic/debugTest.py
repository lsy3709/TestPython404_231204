# 문자열의 내용을 역순으로 출력해보기. 
str = "hi lsy"
reverseStr = ""
for char in str:
  reverseStr = char + reverseStr
print(f"문자열 거꾸로 출력해보기: {reverseStr}")