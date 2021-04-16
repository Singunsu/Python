'''
# if

money = 5000
age = int(input("나이 입력 : "))

if age >= 20 :
    money += 5000
    print(money)



#if else

num = int(input("정수 입력 : "))
if num %2 == 0:
    print("짝수(even) 입니다.")
else:
    print("홀수(odd) 입니다.")
    


#if elif else

score = int(input("점수 입력 : "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")




#iteration.py

dan = int(input("단 입력 : "))
for i in [1, 2, 3, 4, 5, 7, 8, 9]:
    print(dan, "x", i, "=", (dan*i))

na = int(input("나누기 입력 : "))
for a in range(1, 10):
    print(na, "x", a, "=", (na/a))




#sum
    ' 줄을 바꿀 때 ":" '
    ' 첫 줄을 출력할 때 end=="" '
    ' 여기 뒤에 2의 존재는 앞의 101에 2로 나눈 것 '

sum = 0
for i in range(1, 101, 2): '여기 뒤에 2의 존재는 앞의 101에 2로 나눈 것 '
    sum += i

    print(sum)




bum = 0
for a in range(1, 11):
    if a < 10:
        print(a, " + " , end="")
    else:
        print(a, " = ", end="")
    bum += a

    print(bum)




#factorial.py

n = int(input("정수 입력 : "))
fact = 1

'''






