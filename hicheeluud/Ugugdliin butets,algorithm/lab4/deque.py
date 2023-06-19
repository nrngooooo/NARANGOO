class Deque:
    def __init__(self):
        self.__data = []

    #hoino ni element nemeh funkts
    def end(self,e):
        self.__data = self.__data + [e]
        a = self.__data
        print(a)
    #urd ni element nemeh funkts
    def front(self,e):
        self.__data =  [e] + self.__data
        a = self.__data
        print(a)
    #daraallin urtiig hevleh funkts
    def len(self):
        a=0
        for i in self.__data:
            a=a+1
        return a
    #hooson esehiig shalgah funkts
    def isempty(self):
        if self.len()==0:
            return True
        else :
            return False
    #hamgiin suuliin elemtiig hevleh funkts
    def last(self):
        return self.__data[-1]
    #hamgiin ehnii elemtiig hevleh funkts
    def first(self):
        return self.__data[0]
    #daraallin urdaas ni ustgah funkts
    def left(self):
        if self.isempty():
            return "Жагсаалт хоосон байна"
        else:
            a = self.__data[0]
            self.__data=self.__data[1:]
            return a
    #daraallin hoinoos ni ustgah funkts
    def right(self):
        if self.isempty():
            return "Жагсаалт хоосон байна"
        else:
            a = self.__data[-1]
            self.__data=self.__data[:-1]
            return a