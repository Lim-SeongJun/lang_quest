import random

rn = random.sample(range(1,10),3)

ST = 0
BL = 0
count = 0

print("="*10,"숫자야구게임에 온것을 환영합니다","="*10)

while(ST<3):
    num = input("1부터 9까지의 숫자 중 3개를 입력해주세요 : ")
    if(num.isdecimal()==1): # 숫자로만 구성되어있을 경우
        if(len(num)==3): # 숫자가 3개 입력된 경우
            if(num[0]==num[1] or num[0]==num[2] or num[1]==num[2]): # 숫자 3개가 같은경우
                print("숫자가 중복되지않게 다시 입력해주세요")
                continue
        elif(len(num)<3): # 숫자가 3개미만 입력된 경우
            print("숫자가 부족합니다. 다시 입력해주세요")
            continue
        elif(len(num)>3): # 숫자가 3개초과로 입력된 경우
            print("숫자가 많습니다. 다시 입력해주세요")
            continue
    elif(num.isdecimal()==0): #숫자가 아닌 다른 문자가 있을경우
        print("숫자만 입력해주세요")
        continue
    ST=0
    BL=0
    for i in range(0,3):
        for j in range(0,3):
            if(num[i]==str(rn[j]) and i==j): #숫자위치와 숫자가 일치하면 스트라이크+1
                ST+=1
            elif(num[i]==str(rn[j]) and i!=j): #숫자위치는 다르나 숫자가 일치하면 볼+1
                BL+=1
    print(ST,"스트라이크",BL,"볼")
    count+=1
print(count,"번 만에 정답")