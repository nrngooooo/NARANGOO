#daal1
# s = "django"
# print(s[0])
# print(s[5])
# print(s[0:4])
# print(s[1:4])
# print(s[4:])
# print(s[::-1])

#daal2
# l=[3,7,[1,4,'hello']]
# l[2][2]='goodbye'
# print(l)

#daal3
d1={'simple_key': 'hello'}
print(d1['simple_key'])

d2={'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1])

#daal4
# mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]
# print(set(mylist))

#daal5
# age=4
# name= str("Sammy")
# print('Hello my dogs name is ' + str(name) + ' and he is ' + str(age) + ' years old')
# print(f'Hello my dogs name is {name} and he is {age} years old')

#daal6-a 1-10 hurtelh toog while ashiglan hevleh 
# a=1
# while a<11:
#     print(a)
#     a+=1
#daal6-b 100-10 hurtelh toog break ashiglan hevleh 
# b=100
# while b>9:
#     print(b)
#     if b==10:
#         break
#     b-=1
#daal6-c 1-50 hurtelh toonuudaas tegsh too hevleh /break ashiglasan/
# c=0
# while c<51:
#     print(c)
#     if c==50:
#         break
#     c+=2
    # 1-50 hurtelh toonuudaas tegsh too hevleh-2
# i=0
# while i<51:
#     print(i)
#     i+=2

#daal6-d 1-10 hurtelh toonuudas hamgiin ehnii tegsh toog break ashiglan hevleh 
# d=0
# while d<10:
#     print(d)
#     if d==2:
#         break 
#     d+=2


#daal7 python-s h hasaj hevleh 
# a='Python'
# a=a.replace('h', '')
# print(a)

#daal7 1-50 hurtelh toonuudas tegsh toog continue ashiglan hevleh 
# k=0
# while k<51:
#     print(k)
#     k+=2
#     if k==1:
#         continue

# for i in range(0, 51, 2):
#     if i==0:
#         continue
#     print(i)

#daal7 1-10 hurtelh toonuudaas tegsh toog continue break ashiglan hevleh 
# i=0
# while i<=10:
#     print(i)
#     i+=2
#     if i==0:
#         continue
#     elif i==11:
        # break

#1-10 hurtelh toonuudaas hamgiin suulciin tegsh toog continue break ashiglan hevleh 
# for i in range(0, 11, 2):
#     if i==0:
#         continue
#     if i==2:
#         continue
#     if i==4:
#         continue
#     if i==6:
#         continue
#     if i==8:
#         continue
#     if i==11:
#         break
#     print(i)
#daal8 Гараас ямар нэгэн тоон утга авч оронгийн нийлбэрийг хэвлэх
# a=int(input())
# b=a%10
# c=a%1
# print(c,b)