from datetime import datetime, timedelta
from lab12 import SortedMap
class Map(SortedMap):
    def __init__(self, init=None):
        if init is not None:
            self.__dict__.update(init)

    def __getitem__(self, key):
        try:
            return self.__dict__[key]
        except KeyError:
            print(f"{key} утгатай key алга байна ")

    def __setitem__(self, key, val):
        now = datetime.now()
        key = now.strftime("%Y-%m-%d %H:%M:%S")
        while key in self.__dict__:
            now = now + timedelta(minutes=1)
            key = now.strftime("%Y-%m-%d %H:%M:%S")
        self.__dict__[key] = val

    def __delitem__(self, key):
        try:
            del self.__dict__[key]
        except KeyError:
            print(f" {key} утгатай key алга байна")

    def __contains__(self, key):
        return key in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def __repr__(self):
        return self.__dict__

    def get(self, key, d=None):
        return self.__dict__.get(key, d)

    def setdefault(self, key, d):
        return self.__dict__.setdefault(key, d)

    def pop(self, key, d=None):
        return self.__dict__.pop(key, d)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()
M = Map()
M["1"] = 2
M["2"] = 5
M["3"] = 8
M["4"] = 9

print(list(M.keys()))
print(list(M.values()))
print(list(M.items()))
# print(M.setdefault('2023-05-12 11:28:07', 2))
print(M.find_min())
print(M.find_max())
print(M.find_gt('2023-05-12 15:32:07'))

print(M.find_le('2023-05-12 15:32:56'))
print(M.find_it('2023-05-12 15:32:58'))
print(M.find_ge('2023-05-12 15:32:07'))