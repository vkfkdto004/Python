# -*- coding: utf-8 -*-
"""2023.05.15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rqUPCE7sgQfZfmUfmiJll7ZcPy9urnqX
"""

a=365
b=0b101101101
c=0o555
d=0x16d
print(a)
print(b)
print(c)
print(d)

type(a)

fa=3.14
fb=-3.14
fc=3.1415e2
fd=3.1415e-2
print(fa)
print(fb)
print(fc)
print(fd)

print(type(fa))

kor=95
eng=60
math=75
coding=100
result=((kor+eng+math+coding)/4)
print(result)

an_apple=27
an_example=42

print(an_apple)
print(an_example)

an_example??

ba=True
bb=False
print(ba and ba)
print(bb and bb)
print(ba and bb)
print(bb and ba)
print()
print(ba or ba)
print(bb or bb)
print(ba or bb)
print(bb or ba)

a=10
b=5
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

print(bool(""))
print(bool([]))
print(bool(()))
print(bool(0))

sa = "Hello world"
sb = "Tom's favorite food"
sc = '"You are right."I said.'
sd = "Tom's favorite\nfood"
se = '"You are right.".\nI said'
sf = '12\\n34'
print(sa)
print(sb)
print(sc)
print(sd)
print(se)
print(sf)

'this is the first half' + 'and this is second half'

'this is ' *3

eng = 80
result = 'english : ' + eng + '점'
print(result)

eng = 80
result = 'english : ' + str(eng) + '점'
print(result)

len('this is the first half' + 'and this is second half')

a='this is a string'
print(a[0])
print(a[-1])
print(a[4])
print(a[0:6])
print(a[-6:])
print(a[:])

a.replace('string', 'rope')

name = "KIMWOOSEOP"
print("My name is %s."%name)

age = 25
print("My age is %d." %age)

year = 2023
month = 5
day = 15
print("{}-{}-{}".format(year,month,day))

year = 2023
month = 5
day = 15
print("%2d-%02d-%02d"%(year,month,day))

height = 172.5
print("키는 %.2f 입니다"%height)

e = 3
print("I have {} children".format(3))
print("I have {} children".format("three"))
print("I have {} children".format(e))
print("I have {} children {}".format(3.14,"wow"))

print("This is %d%% True!" %100)
print('%10s' % 'Good')
print('%-10s' % 'Good')
pi = 3.141592
print("%.2f"%pi)
print("%20.2f"%pi)

print('{:<20}'.format('good'))
print('{:>20}'.format('good'))
print('{:^20}'.format('good'))
print('{:*^20}'.format('good'))

a = 4.5560
b = 'Argentine Pesos'
c = 1
print("%.2f %s are worth US$%d"%(a,b,c))
print("{0:.2f} {1} are worth US${2}".format(a,b,c))
print("{{우리집}}에 {0} 놀러와요".format("자주"))

a = 3
b = 'wow'
print(f"I have {a} children {b}")
print(f"I have {a+2} children {b}")

print(f'{{good}}''{day}')

sa = "Korean culture"
print(sa.count("u"))
print(sa.index("K"))
print(" ".join(sa))
print(",".join('123456789'))

a = "Korean culture"
print(a.upper())
print(a.lower())

a = "      Korean      "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = "Korean culture"
print(a.replace("Korean", "American"))
print(a.split())
b = "Korean&culture"
print(b.split("&"))

print("C:\\nano")
a = "990316-2030998"
print("IU =","".join("990316-2030998"))
print(a[7])

b="a:b:c:d"
print(b)
print(b.replace(":", "@"))

c = "a&b&c&d"
print(c)
print(c.split("&"))

a = "720"
print(int(a))
b = 100
print(str(b))

game = "짝홀짝홀짝홀"
print(game[::-2])

PN = "010-1234-5678"
result = PN[0:3] + PN[4:8] + PN[9:13]
print(result)
print(PN.replace("-", ""))

c = "https://www.samsung.com"
print(c[-3:])

a = []
print(a)
b = [1,2,3,4,5]
print(b)
c = ["red","blue","yellow"]
print(c)
d = [1,2,"red","blue"]
print(d)
e = [1,2,["red","blue"]]
print(e)