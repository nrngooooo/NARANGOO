class Node:
    def __init__(self, e):
        self.data =e
        self.address = None
    
class LinkedList:
    def __init__(self, *values):
        self.start_node=None
        for value in values:
            self.insert_end(value)
###################################Nodes хэвлэх##############################################
    def print_list(self):
        if self.start_node is None:
            print('жагсаалт хоосон байна!')
            return
        else:
            a = self.start_node
            while a is not None:
                print(a.data," ")
                a = a.address
###################################Эхэнд нэмэх##############################################
    def insert_front(self, data):
        new_node = Node(data)
        new_node.address = self.start_node
        self.start_node = new_node
###################################Хойно нэмэх##############################################
    def insert_end(self, data):
        new_node =Node(data)
        if self.start_node is None:
            self.start_node=new_node
            return
        a =self.start_node
        while a.address is not None:
            a =a.address
        a.address = new_node

#########################################Утга нэмэх#########################################
    def insert_index(self, index, data):
        if index == 1:
            self.insert_front(data)
        i = 1
        a = self.start_node 
        while i < index - 1 and a is not None:
            a = a.address
            i = i+1 

        if a is None:
            print("хэтэрсэн байна ")
        else:
            new_node = Node(data)
            new_node.address = a.address
            a.address = new_node
#########################################Тоолох#########################################
    def get_count(self):
        if self.start_node is None:
            return 0
        a = self.start_node
        count = 0 
        while a is not None:
            count = count + 1
            a =a.address
        return count
    
#########################################Хайх#########################################
    def search_item(self, s):
        if self.start_node is None:
            print("жагсаалт хоосон байна")
            return
        else :
            a = self.start_node
            while a is not None :
                if a.data == s:
                    print(f'Таны хайсан үр дүн олдсон {s}')
                    return True
                a = a.address
            else :
                print(f'таны хайлт олдсонгүй {s}')
                return False
#########################################Устгах#########################################
    def delete_start(self):
        if self.start_node is None:
            print("Жагсаалт хоосон!!!")
            return
        self.start_node = self.start_node.address
    def delete_end(self):
        if self.start_node is None:
            print("Жагсаалт хоосон!!!")
            return
        n = self.start_node
        while n.address.address is not None:
            n = n.address
        n.address = None
    def delete_node(self, value):
        if self.start_node is None:
            return
        if self.start_node.data == value:
            self.start_node = self.start_node.address
            return
        prev_node = self.start_node
        while prev_node.address is not None and prev_node.address.data != value:
            prev_node = prev_node.address
        if prev_node.address is None:
            return
        prev_node.address = prev_node.address.address    


























k= LinkedList()
k.insert_front(12)
k.insert_front(10)
k.insert_front(13)
k.insert_front(20)
k.insert_end(30)
# k.insert_end(24)
# k.insert_end(25)
# k.insert_index(3, 11)
# k.delete_end()
k.delete_end()
# k.delete_start()


k.delete_node(99)
k.print_list()
# k.print_list()



k.search_item(15)
# k.search_item(19)