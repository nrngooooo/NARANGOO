class BankAccount:
    def __init__(self,pin,amount):
        self.amount = amount
        self.pin = pin
            
    def deposit(self,amount):
        self.amount += int(amount)
        print(f"Таны данс {amount}₮-р цэнэглэгдэж нийт үлдэгдэл {self.amount}₮ боллоо. ")
        
    def withdraw(self,amount):
        if self.amount < int(amount):
            print(f"Таны дансны үлдэгдэл хүрэлцэхгүй байна")
            self.get_balance()
        else:
            self.amount -= int(amount)
            print(f"Таны данснаас {amount}₮ хасагдаж нийт үлдэгдэл {self.amount}₮ боллоо.")
        
    def get_balance(self):
            print(f"Таны дансны үлдэгдэл: {self.amount}₮")
                
a = BankAccount('1122',0)    
while 1 > 0:
    print(  "1. Дансны үлдэгдэл шалгах\n"
            "2. Deposit хийх\n"
            "3. Withdraw хийх\n"
            "0. Гарах\n")
    exer = input("Сонголтоо оруулна уу: ")
    try:
        match int(exer):
            case 1:
                pin = input("PIN оруулна уу: ")
                if pin == a.pin:
                    a.get_balance()
                else:
                    print("PIN буруу байна")
            case 2:
                pin = input("PIN оруулна уу: ")
                if pin == a.pin:
                    amount = input("Орлого хийх мөнгөн дүнгээ оруулна уу: ")
                    a.deposit(amount)
                else:
                    print("PIN буруу байна")
            case 3:
                pin = input("PIN оруулна уу: ")
                if pin == a.pin:
                    amount = input("Зарлага хийх мөнгөн дүнгээ оруулна уу: ")
                    a.withdraw(amount)
                else:
                    print("PIN буруу байна")
            case 0:
                break
            case _:
                print(f"{exer} дугаартай сонголт алга !!!\n\n")
    except:
         print("Алдаа гарлаа !!!\n\n")
