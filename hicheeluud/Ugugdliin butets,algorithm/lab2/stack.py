class MyStack: 
    def __init__(self):
        self.__data = []

    def nemeh(self,e):
        self.__data = self.__data + [e]

    def len(self):
        a=0
        for i in self.__data:
            a=a+1
        return a

    def isempty(self):
        if self.len()==0:
            return True
        else :
            return False

    def top(self):
        return self.__data[-1]
    

    def hasah(self):
        if self.isempty():
            return "Жагсаалт хоосон байна"
        else:
            a = self.__data[-1]
            self.__data=self.__data[:-1]
            return a