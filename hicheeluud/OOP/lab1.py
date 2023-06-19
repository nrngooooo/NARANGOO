#d1
# a = input("1-7 iin hoorond too oruulna uu:")
# if a.isdigit(): 
#     a=int(a)
#     if a==1: 
#         print('Today is Monday')
#     elif a==2:
#         print('Today is Tuesday')
#     elif a==3:
#         print('Today is Wednesday')
#     elif a==4:
#         print('Today is Thursday')
#     elif a==5:
#         print('Today is Friday')
#     elif a==6:
#         print('Today is Saturday')
#     elif a==7:
#         print('Today is Sunday')
#     else:
#         print('error')
# else:
#     print('Тоо оруулна уу')

# # d2-1 Гараас 3 тоо авч хамгийн их утгыг хэвлэнэ
# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:
#     print(a)
# elif b>c:
#     print(b)
# elif c>b:
#     print(c)

# d2-2 Гараас 3 тоо авч хамгийн бага утгыг хэвлэнэ
# a=int(input())
# b=int(input())
# c=int(input())
# if a<b:
#     print(a)
# elif b<c:
#     print(b)
# elif c<b:
#     print(c)

# d2-3 Гараас 3 тоо авч дундаж утгыг хэвлэнэ
# a=int(input())
# b=int(input())
# c=int(input())
# if a<b<c:
#     print(b)
# elif b<c<a:
#     print(c)
# elif b<a<c:
#     print(a)

# d3
# d1={'username': 'admin', 'password': 'mandakh'}
# a=input('Username: ')
# b=input('Password: ')
# if a=='admin' and b=='mandakh':
#     print(f'hi? {a} welcome')
# else:
#     print('error')

# d4
x = str(input())
s=0
for y in x:
    if y=="a":
        s=s+1
print(f'{x} Энэ үгэнд {s} а үсэг байна')
