num = int(input("자연수를 입력해주세요 : ", ))
count = 0
for i in range(1,num+1):
    sum = 0
    for j in range(i,num+1):
        sum+=j
        if(sum==num):
            count+=1
            break
        elif(sum>num):
            break
print(count)