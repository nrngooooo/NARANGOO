# Даалгавар-1 Гараас 3 тоо авч хамгийн, бага болон дундаж-г хэвлэх функц бичих
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
#     print(f"Хамгийн их: {a}")
# elif b>a and b>c:
#     print(f"Хамгийн их: {b}")
# elif c>b and c>a:
#     print(f"Хамгийн их: {c}")
# if a<b and a<c:
#     print(f"Хамгийн бага: {a}")
# elif b<a and b<c:
#     print(f"Хамгийн бага: {b}")
# elif c<b and c<a:
#     print(f"Хамгийн бага: {c}")
# print(f"3 toonii dundaj {(a+b+c)/3}")

#Хамгийн бага
# a=int(input())
# b=int(input())
# c=int(input())
# x='Хамгийн их:'
# y='Хамгийн бага:'
# z='Дундаж:'
# if a<b<c:
#     print(y, a)
# elif b<a<c:
#     print(y, b)
# elif c<b<a:
#     print(y, c)

# Хамгийн их 
# if a>b>c:
#     print(x, a)
# elif b>a>c:
#     print(x, b)
# elif c>b>a:
#     print(x, c)

#Дундаж 
# if a>b>c:
#     print(z, b)
# elif b>c>a:
#     print(z, c)
# elif c>a>b:
#     print(z, a)


#d2 
# Ямар нэг тэмдэгт мөр болон жагсаалтын уртыг хэвлэх функц бичих
# def print_name():
#     a =input()
#     count = 0

#     while True:
#         try:
#             if a[count]:
#                 count += 1
#         except IndexError as e:
#             break
#     print(count)

# print_name()

#d3 
# def useg_oloh(s, c) :
#     res = 0
#     for i in range(len(s)) :        
#         if (s[i] == c):
#             res = res + 1
#     return res
# str=input()
# c = 'a'
# d = 'b'
# f = 'c'
# g = 'd'
# h = 'e'
# print("a:",useg_oloh(str,c), "b:",useg_oloh(str,d), "c:",useg_oloh(str,f), "d:",useg_oloh(str,g),"e:",useg_oloh(str,h))
#d3-a
# import collections 
# print(collections.Counter("collectiomn"))

# d4
# def orchuulga(a):
#     if a=="This is computer":
#         print("Энэ бол компьютер")
#     elif a=="Энэ бол компьютер":
#         print("This is computer")
#     elif a=="good":
#         print("сайн")
#     elif a=="сайн":
#         print("good")
#     elif a=="муу":
#         print("bad")
#     elif a=="bad":
#         print("муу")
#     elif a=="basketball":
#         print("сагсанбөмбөг")
#     elif a=="сагсанбөмбөг":
#         print("basketball")
#     elif a=="volleyball":
#         print("гар бөмбөг")
#     elif a=="гар бөмбөг":
#         print("volleyball")
#     elif a=="ball":
#         print("бөмбөг")
#     elif a=="бөмбөг":
#         print("ball")
#     elif a=="football":
#         print("хөлбөмбөг")
#     elif a=="хөлбөмбөг ":
#         print("football")
#     elif a=="бал":
#         print("pen")
#     elif a=="pen":
#         print("бал")
#     elif a=="ширээ":
#         print("table")
#     elif a=="table":
#         print("ширээ")
#     elif a=="цаас":
#         print("paper")
#     elif a=="paper":
#         print("цаас")
#     elif a=="note":
#         print("дэвтэр")
#     elif a=="bag":
#         print("цүнх")
#     else:
#         print("Манай толь бичигт ийм үг алга")
# a=input()
# print(orchuulga(a))

# d5 
# Палиндром
# def Palindrom(a):
#     return a==a[::-1]
# a=input()
# wrd=Palindrom(a)
# if wrd:
#     print("true")
# else:
#     print("false")
    
# d6 
# SUM функц

# def sum_numbers(numbers):
#      total = 0
#      for number in numbers:
#          total += number
#      return total
# sum_numbers([1, 2, 3, 4, 5])
# sum_numbers([])

#d7 
# регистрийн дугаарыг “1990-02-01” форматаах хэвлэх функц бичих
# g=input()
# def registerToDate(regNum):
#     return '19'+ regNum[2:4] + '-' + regNum[4:6] + '-' + regNum[6:8]
# print(registerToDate(g))

# хүний овог болон нэрийг бүтнээр нь авч “П.Зоригтбаатар” форматаар хэвлэх функц бичих
# def shortName(ovog,ner):
#     return ovog[0] + "." +ner
# if __name__ == '__main__':
#     print(shortName('Пүрэв-Очир','Зоригтбаатар'))

# хүний овог болон нэрийг бүтнээр нь авч “Пүрэв-Очир овогтой Зоригтбаатар” форматаар хэвлэх функц бичих
# def shortName(ovog,ner):
#     return ovog + " овогтой " +ner
# if __name__ == '__main__':
#     print(shortName('Пүрэв-Очир','Зоригтбаатар'))
# d8
# carPrice = ['2500', '35500', '17500', '4000']
# list2 = []
# for i in range(len(carPrice)):
#     t = int(carPrice[i])*3300
#     list2.append(t)
# print(list2)

# carPrice=['$2500', '$35500', '$17500', '$4000']
# first=2500*3300
# print("price of first car: ", first)
# second=35500*3300
# print("piece of second car: ", second)
# third=17500*3300
# print("piece of thirs car: ", third)
# fourth=4000*3300
# print("piece of fourth car: ", fourth)

#d9
# Xаалт ( | )- р зааглаж хүмүүсийн нэрийг тэмдэглэсэн бөгөөд хүн тус бүрийн нэрийн салгаж хэвлэнэ үү.
# a = input().split("|")
# for i in range(len(a)):
#     print(a[i])

#d10 
# l= input("Та тэмдэгт оруулна уу:")
# l=l.count(input("та тоолох тэмдэгтээ оруулна уу:"))
# print("үр дүн:",l) 

def useg_oloh(s, c) :
    res = 0
    for i in range(len(s)) :
        if (s[i] == c):
            res = res + 1
    return res
str=input("Та тэмдэгт оруулна уу:")
c=input("та тоолох тэмдэгтээ оруулна уу:")
print("үр дүн:",useg_oloh(str, c))



# carPrice=['$2500', '$35500', '$17500', '$4000']

# first=2500*3300
# print("price of first car: ", first)
# second=35500*3300
# print("piece of second car: ", second)
# third=17500*3300
# print("piece of thirs car: ", third)
# fourth=4000*3300
# print("piece of fourth car: ", fourth)

#3
# import collections 
# print(collections.Counter("collectiomn"))
#7 
# g=input()
# def registerToDate(regNum):
#     return '19'+ regNum[2:4] + '-' + regNum[4:6] + '-' + regNum[6:8]
# print(registerToDate(g))
