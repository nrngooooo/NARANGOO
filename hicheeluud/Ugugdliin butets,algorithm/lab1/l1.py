# toonuud = []
# niilber = 0

# a = int(input('ta heden too oruulah ve?'))

# for i in range(a):
#     num = int(input(f'Ta {i+1} deh toogoo oruulna u:'))
#     toonuud.append(num)

# ih = toonuud[0]
# baga = toonuud[0]

# for too in toonuud:
#     niilber += too

#     if ih < too:
#         ih = too
#     if baga > too:
#         baga = too

# print(f"Dundaj {niilber/a}")
# print(f"Hamgiin baga {baga} ")
# print(f"Hamgiin ih {ih}")

# n = int(input("Та хэдэн тоо оруулах вэ?:"))
# mylist = []
# for _ in range(n):            
#     mylist.extend(list(map(int, input("Та тоогоо оруулна уу:").rstrip().split())))
#     def bugd(mylist):
#         sum = mylist[0]
#         min = mylist[0]
#         max = mylist[0]
#         avg =mylist[0]
#         for i in range(1,len(mylist)):
#             sum += mylist[i]
#             if mylist[i]< min:
#                 min = mylist[i]
#             if mylist[i]> max:
#                 max =mylist[i]
#         avg =sum/ len(mylist)
#         return  avg , min , max
#     result = bugd(mylist)
# print("Дундаж:", result[0])
# print("Хамгийн бага:", result[1])
# print("Хамгийн их:", result[2])

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
#         print('!!!!!!!!!!!')
# else:
#     print('Тоо оруулна уу')

############################################INHERITANCE####################################################
# class Animal:
#    def __init__(self, turul, animal):
#     self.turul = turul
#     self.aname = animal
#    def __str__(self):
#     return self.turul + ' төрлийн ' + self.aname

# class Bird(Animal):
#     def __init__(self, turul, animal, action):
#         Animal.__init__(self,turul, animal)
#         self.action = action
#     def ontslog(self):
#         return self.action
# shuvuu = Animal('African Grey', 'Тоть')
# print(shuvuu.__str__())
# shuvuu = Bird('African Grey', 'Тоть','хүний дуу хоолойг дууриаж чадна ө.х авиа дууриаж чадна' )
# print(f'Онцлог зан чанар: {shuvuu.ontslog()}')


# ###############################POLIMORPHISM##############################################################
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name

# class Animals(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#     def leg(self):
#         return self.name + ' 4 хөлтэй'

# class Hun(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#     def leg(self):
#         return self.name + ' 2 хөлтэй'

# class Birds(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#     def leg(self):
#         return self.name + ' 2 хөлтэй мөн далавчтай'

# d = Animals('Ихэнх хөхтөн амьтад')
# print(d.leg())

# c = Hun('Хүн')
# print(c.leg())

# g = Birds('Шувууд')
# print(g.leg())
print(2+2*3-1)