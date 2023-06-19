from lab12 import M

newMap = M
print(list(newMap.items()))
# print(newMap.setdefault('2023-05-12 11:28:07', 2))

newMap.find_min()
newMap.find_max()
newMap.find_gt('2023-05-14 23:25:22')

newMap.find_le('2023-05-14 15:50:35')
newMap.find_it('2023-05-12 15:50:35')

newMap.find_ge('2023-05-13 15:52:35')