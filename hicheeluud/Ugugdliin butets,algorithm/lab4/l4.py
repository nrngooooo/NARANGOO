from deque import Deque

a= Deque()
a.end(5)
a.front(3)
a.front(7)

print(f'дарааллын эхний элемент нь: {a.first()}')
print(f'дарааллаас хасагдсан нь : {a.right()}')
print(f'дарааллын урт нь: {a.len()}')
print(f'дарааллаас хасагдсан нь : {a.right()}')
print(f'дарааллаас хасагдсан нь : {a.right()}')
a.front(6)
print(f'дарааллын сүүлийн элемент нь: {a.last()}')
a.front(8)
print(f'дараалал хоосон эсэх нь:{a.isempty()}')
print(f'дарааллын сүүлийн элемент нь: {a.last()}')