from queue import Queue

a= Queue()
a.enqueue(5)
a.enqueue(3)

print(f'дарааллын урт нь: {a.len()}')
print(f'дарааллаас хасагдсан нь : {a.dequeue()}')
print(f'дараалал хоосон эсэх нь:{a.isempty()}')
print(f'дарааллаас хасагдсан нь : {a.dequeue()}')
print(f'дараалал хоосон эсэх нь:{a.isempty()}')
print(f'дарааллаас хасагдсан нь : {a.dequeue()}')
a.enqueue(7)
a.enqueue(9)
print(f'дарааллын эхнийх нь: {a.first()}')
a.enqueue(4)
print(f'дарааллын урт нь: {a.len()}')

print(f'дарааллаас хасагдсан нь : {a.dequeue()}')
