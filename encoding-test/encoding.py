import sys

# 엔코딩이 어디까지 겹치는지 테스트하기 위해 사용함
def TestEncoding(pyString):
    print("<< {} >>".format(pyString))
    #encoding하기
    cp949 = str.encode(pyString, encoding="cp949")
    unicode = str.encode(pyString, encoding="utf-8")
    print("--------cp949 test result--------")
    try:
        print("cp949로 읽음: " + str(cp949, "cp949"))
    except :
        print("cp949로 읽기 실패")

    try:
        print("utf-8로 읽음: " + str(cp949, "utf-8"))
    except :
        print("utf-8로 읽기 실패")
    print("--------unicode test result--------")
    try:
        print("cp949로 읽음: " + str(unicode, "cp949"))
    except :
        print("cp949로 읽기 실패")

    try:
        print("utf-8로 읽음: " + str(unicode, "utf-8"))
    except :
        print("utf-8로 읽기 실패")

    print("-"*30, end="\n\n")
        
TestEncoding("Abc")
TestEncoding("ㄱㄱㄱ")
TestEncoding("가나다")
TestEncoding("@#$!$")
TestEncoding("Abc.ㄱㄴㄷ.가나다.갇낟닫")