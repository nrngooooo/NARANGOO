from stack import MyStack
a= MyStack()
a.nemeh(5)
a.nemeh(3)

print(f'жагсаалтын урт нь: {a.len()}')
print(f'жагсаалтын хасагдсан нь: {a.hasah()}')
print(f'жагсаалт хоосон эсэх нь: {a.isempty()}')
print(f'жагсаалтын хасагдсан нь: {a.hasah()}')
print(f'жагсаалт хоосон эсэх нь : {a.isempty()}')
print(f'жагсаалтын хасагдсан нь: {a.hasah()}')
a.nemeh(7)
a.nemeh(9)
print(f'жагсаалтын cүүлийн орон нь: {a.top()}')
a.nemeh(4)
print(f'жагсаалтын урт нь: {a.len()}')
print(f'жагсаалтын хасагдсан нь: {a.hasah()}')
a.nemeh(6)
a.nemeh(8)
print(f'жагсаалтын хасагдсан нь: {a.hasah()}')