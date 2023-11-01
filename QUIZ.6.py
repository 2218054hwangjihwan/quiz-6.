

#(반복문) 종료 번호(4번)가 나올때까지 반복
#(함수, 사용자 입력 함수) input, print 등
#(조건문) if, while 등
#안전율(안전계수) = 허용 응력 / 허용 하중

MODE=0
while(MODE!=4):
    X=0
    Y=0
    RESULT=0
    MODE_2=0
    print("========================")
    print("   안전율 계산기  ")
    print("     제작자 : 황지환    ")
    print("1 - 안전율(안전계수)")
    print("2 - 허용 응력")
    print("3 - 허용 하중")
    print("4 - 종료")
    print("=======================")
    MODE=int(input("어떤 것을 이용하시겠어요? : "))
    if (MODE==1):
        X=float(input("허용 응력을 입력해주세요. : "))
        Y=float(input("허용 하중을 입력해주세요. : "))
        RESULT=X/Y
        print("안전율(안전계수) :",RESULT)
    if (MODE==2):
        X=float(input("안전율(안전계수)를 입력해주세요. : "))
        Y=float(input("허용 하중을 입력해주세요. : "))
        RESULT=X*Y
        print("허용 응력 :",RESULT)
    if (MODE==3):
        X=float(input("안전율(안전계수)를 입력해주세요. : "))
        Y=float(input("허용 응력을 입력해주세요. : "))
        RESULT=Y/X
        print("허용 하중 :",RESULT)
    if (MODE==4):
        print(" 종료되었습니다.")
