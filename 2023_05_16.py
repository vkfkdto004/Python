# -*- coding: utf-8 -*-
"""2023.05.16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MEudMX7-q0m8Wk9y5Ifv2xDWJQz5fD4S
"""

b = [1,2,3,4,5]
print(b[0])
print(b[0] + b[2])
print(b[4])

new_a = [1,2,3,4,5,["a","b","c","d"],7,8,9]
print(new_a[:])
print(new_a[0])
print(new_a[8])
print(new_a[5])
print(new_a[5][2])

b = [1,2,3,4,5]
print(b[0:4])

c = "12345"
print(c[0:4])

print(b[3:])

new_a = [1,2,3,4,5,["a","b","c","d"],7,8,9]
print(new_a[0:6])
print(new_a[:5:2])
print(new_a[0:4:3])
print(new_a[0:5:4])
print(new_a[5][0:2])

a = [1,2,3,4]
b = [6,7,8,9]

print(a+b)
print(a*2)
print(len(a))

k = [12345678]
print(len(k))

m = '123456789'
print(len(m))

c = "good"
print(str(b) + c)

new_c = ['good']
print(b + new_c)

a = [1,2,3,4,[a,b,c]]
b = [6,7,8,9]
print(len(a))
print(sum(a[0:4]))
print(sum(b))
print(max(b))
print(min(b))
b.remove(6)
print(b)

b = [6,7,8,9]
del b[0:3]
print(b)
print(str(b[0]))

b = ["6","7","8","9"]
b.append("10")
print(b)

b.append(["11","12"])
print(b)

c = ["6","9","8","7"]
c.sort()
print(c)

d = ["x","z","y"]
d.sort()
print(d)

c = ["6","7","8","9"]
c.sort()
c.reverse()
print(c)

c = ["6","7","8","9"]
print(c.index("9"))
#print(c.index("5"))
c.append("10")
print(c)
c.insert(0,"5")
print(c)

we = ["We","are","the","world"]
print(" ".join(we))

a = [8,8,8]
print(a+[[1,5]])
a.extend(["cola"])
print(a)

m_r = ["알라딘","토이스토리","기생충"]
m_r.append("롱 리브 더 킹")
print(m_r)
m_r.insert(2,"슈퍼맨 리턴즈")
print(m_r)
m_r.remove("기생충")
print(m_r)

A = ["BTS","엑소","뉴이스트"]
B = ["Black Pink","아이즈원","트와이스"]
AB = A+B
print(AB)

num = [1,2,3,4,5,6,7,8,9,10]
print(max(num))
print(min(num))
result = sum(num)
print(result)
print(result/10) #평균 

cook = ["피자","김밥","만두","양념치킨","족발"]
print(len(cook))

price = ['20190625',1000,3000,4000,5000,7000]
print(price[1:])

num = [1,2,3,4,5,6,7,8,9,10]
print(num[::2])
print(num[1::2])
num.reverse()
print(num)

string = "구글/아마존/페이스북"
wish = string.split("/")
print(wish)

a = ()
b = (1,)
c = (1,2,3)
print(a)
print(b)
print(c)

x,y,z = 1,2,3
print(x)
print(y)
print(z)
print(x,y,z)

c = 1,2,3
e = 1,2,("ab","cd"),3,4
print(e[:])
print(c+e)
print(c*2)
print(len(c))

DS = ()
print(type(DS))

a = (1,)
print(type(a))

t = 1,2,3,4
print(type(t))

x = ("a","b","c")
x = list(x)
x[0] = "A"
x = tuple(x)
print(x)
 
wish = ("google","amazon","facebook")
li = list(wish)
print(li)

wish = ["google","amazon","facebook"]
tu = tuple(wish)
print(tu)

my_data = 1,2,3
a,b,c = my_data
print(a+b+c)

a = 4,2,1,8
print(a+(9,))

dic = {
    "이름" : "mina",
    "성별" : "여성",
    "나이" : 30
    }
print(dic["성별"])
print(dic["나이"])
print(dic.keys())

score = {
    "A" : 99,
    "B" : 91,
    "C" : 83,
    "D" : 100
}
print(score["C"])

brother = {
    "형님들" : ["김대현","오창진","권재훈","김우섭"]
}
print(brother["형님들"])

a = {"gender" : "Female","age":30,"name":"Kristina"}

print(a.keys())
print(list(a.keys()))
print(a.values())
print(a.items())
print(a.clear())
print(a)

a = {"gender" : "Female","age":30,"name":"Kristina"}
print(a.get("gender"))#a["gender"]
print(a.get("height"))
print(a.get("height","?"))
print("gender" in a)
print("height" in a)

s1 = set([1])
print(s1)

s2 = set()
print(s2)

sc = set('abcdef')
print(sc)
print(type(sc))

sl = list(sc)
print(sl[1])
print(type(sl))

x = {1,2,3,4,5}
y = {3,4,5,6,7}

print(x & y) #교집합
print(x | y) #합집합 
print(x - y) #차집합 
print(y - x)
print(x ^ y) #여집합

DS = {}

icecream = {
    "메로나" : 1000,
    "폴라포" : 1200,
    "빵빠레" : 1800
}
print(icecream)

icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)

print("메로나 가격 :", icecream["메로나"])

icecream["메로나"] = 1200
print("메로나 가격 : ", icecream["메로나"])

del icecream["메로나"]
print(icecream)

inventory = {
    "메로나":[300,20],
    "비비빅":[400,3],
    "죠스바":[250,100]
}
print(inventory.get("메로나")[0])
print(inventory.get("메로나")[1])

inventory["월드콘"] = [500,7]

print(inventory)

icecream_2 = {
    "이름" : ["메로나","폴라포","빵빠레"],
    "가격" : [1000,1200,1800]
}
icecream_2["이름"] += ["죠스바","월드콘"]
icecream_2["가격"] += [1200,1500]
print(icecream_2)

x1 = 2
x2 = 5
print(x1 + x2)
print(x2 - x1)
print(x1 * x2)
print(x1**2)
print(x1**(1/2))
print(x2/x1)
print(x2//x1)
print(x2%x1)

a = 20
a+=5
print(a)
a-=10
print(a)
a*=2
print(a)
a/=3
print(a)

c=3
b=2
c*=(2+b)
print(c)
c*=(b-5)
print(c)

a = 95
print(a == 90) #같은지
print(a != 90) # 다른지
print(a > 90) # a가 큰지 
print(a < 90) # a가 작은지 
print(a >= 90) # a 가 이상인지 
print(a <= 90) # a 가 이하인지
print(a >= 90 and a <= 100) # 90이상 100 이하 
print(100 <= a <= 110) # 100이상 110 이하 
print(70 <= a <= 80) # 70이상 80 이하

x = 10
y = 20
print("x = "+str(x)+","+ "y = "+str(y))

score1 = 80
score2 = 87
sum = score1 + score2
avg = sum/2

print("두 과목 점수 : {},{}".format(score1,score2))
print("합계 : {} , 평균 : {}".format(sum, avg))

year = 2023
month = 5
day = 16
print(year,month,day,sep="-")

a = "안녕하세요."
b = "반갑습니다."

print(a,b,end="\n")
print(a,b,end="")

