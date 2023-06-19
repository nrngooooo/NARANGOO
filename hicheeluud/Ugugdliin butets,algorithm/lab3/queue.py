class Queue: 
    def __init__(self):
        self.__data = []

    def enqueue(self,e):
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

    def first(self):
        return self.__data[0]
    
    def dequeue(self):
        if self.isempty():
            return "Жагсаалт хоосон байна"
        else:
            a = self.__data[0]
            self.__data=self.__data[1:]
            return a

# class Deque(Queue):
#     def __init__(self):
#         self.__data = []
#     def bnemeh(self,e):
#         self.__data = self.__data + [e]
#     def znemeh(self,e):
#         self.__data = self.__data + [e]