class Restaurant:
        def __init__(self, foodList):
            self.__foods__ = foodList
            self.__order__ = []
            self.price = 0

        def order(self):
            while 1 > 0:
                print("___________________________\n\n"
                    f"1. {self.__foods__[1][0]} :  {self.__foods__[1][1]}\n"
                    f"2. {self.__foods__[2][0]} :  {self.__foods__[2][1]}\n"
                    f"3. {self.__foods__[3][0]} :  {self.__foods__[3][1]}\n"
                    f"4. {self.__foods__[4][0]} :  {self.__foods__[4][1]}\n"
                    "5. Захиалга дуусгах\n"
                    "0. Гарах\n"
                    f"Нийт: {self.price}\n"
                    f"Захиалга:")
                for i in range(len(self.__order__)):
                    print(f"{self.__order__[i][0]}")
                exer = input("Сонголтоо оруулна уу: ")
                match int(exer):
                    case 1:
                        self.__order__.append(self.__foods__[1])
                        self.price += self.__foods__[1][1]
                    case 2:
                        self.__order__.append(self.__foods__[2])
                        self.price += self.__foods__[2][1]
                    case 3:
                        self.__order__.append(self.__foods__[3])
                        self.price += int(self.__foods__[3][1])
                    case 4:
                        self.__order__.append(self.__foods__[4])
                        self.price += int(self.__foods__[4][1])
                    case 5:
                        self.endorder()
                        break
                    case 0:
                        break

        def endorder(self):
            desc = input("1. Төлөх\n"
                        "2. Цуцлах\n")
            match int(desc):
                case 1:
                    print("Манайхаар үйлчлүүлсэнд баярлалаа")
                case 0:
                    return  
foodList = {1:["Цуйван",9500],2:["Өндөгтэй бифштекс",11500],3:["Гуляш",10500],4:["Цай",1100],6:["Нарийн махан хуурга",15000]}
a = Restaurant(foodList)  
while 1 > 0:
    print("___________________________\n\n"
            "1. Хоол захиалах\n"
            "0. Гарах\n"
            "___________________________\n")
    exer = input("Сонголтоо оруулна уу: ")
    match int(exer):
        case 1:
            a.order()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 0:
            break
        case _:
            print(f"{exer} дугаартай сонголт алга !!!\n\n")
