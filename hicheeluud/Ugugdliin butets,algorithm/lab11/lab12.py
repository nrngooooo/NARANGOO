from datetime import datetime, timedelta

class SortedMap(dict):
    def __init__(self):
        self.__dict__ = {}

    def __getitem__(self, k):
        for key, val in self.__dict__.items():
            if val == k:
                return key
        return f"{k} utgatai key oldsongui"

    def __setitem__(self, k, v):
        now = datetime.now()
        key = now.strftime("%Y-%m-%d %H:%M:%S")
        while key in self.__dict__:
            # if the key is already present, add one minute to it
            now = now + timedelta(minutes=1)
            key = now.strftime("%Y-%m-%d %H:%M:%S")
        self.__dict__[key] = v

    def __delitem__(self, k):
        try:
            del self.__dict__[k]
        except KeyError:
            raise KeyError(f"{k} утгатай key алга байна")

    def __len__(self) -> int:
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def get(self, k, d=None):
        return self.__dict__.get(k, d)

    def setdefault(self, k, d):
        return self.__dict__.setdefault(k, d)

    def pop(self, k, d=None):
        return self.__dict__.pop(k, d)
    
    def find_min(self):
        if len(self.__dict__) == 0:
            return None
        min_key = min(self.__dict__.keys())
        return (min_key, self.__dict__[min_key])

    def find_max(self):
        if len(self.__dict__) == 0:
            return None
        max_key = max(self.__dict__.keys())
        return (max_key, self.__dict__[max_key])        
    def find_it(self, k):
        lessThanK = []
        for ke in self.__dict__.keys():
            if k > ke:
                lessThanK.append(ke)
        if lessThanK:
            return print(f"{k}-н утгаас бага бас хамгийн их утгатай түлхүүр нь: {max(lessThanK)}")
        else:
            return print(f"{k}-н утгаас бага бас хамгийн их утгатай түлхүүр олдсонгүй.")

    def find_le(self, k):
        lessThanEqualK = []
        for ke in self.__dict__.keys():
            if k >= ke:
                lessThanEqualK.append(ke)
        if lessThanEqualK:
            return print(f"{k}-с хойшгүй хамгийн их утгатай түлхүүр нь: {max(lessThanEqualK)}, утга: {self.__dict__[max(lessThanEqualK)]}")
        else:
            return print(f"{k}-с хойшгүй түлхүүр олдсонгүй.")

    def find_gt(self, k):
        greaterThanK = []
        for ke in self.__dict__.keys():
            if k < ke:
                greaterThanK.append(ke)
        if greaterThanK:
            return print(f"{k}-с их утгатай түлхүүр нь: {min(greaterThanK)}, утга: {self.__dict__[min(greaterThanK)]}")
        else:
            return print(f"{k}-с их утгатай түлхүүр олдсонгүй.")

    def find_ge(self, k):
        greaterThanEqualK = []
        for ke in self.__dict__.keys():
            if k <= ke:
                greaterThanEqualK.append(ke)
        if greaterThanEqualK:
            return print(f"{k}-с дээшгүй эсвэл тэнцүү хамгийн бага утгатай түлхүүр нь: {min(greaterThanEqualK)}, утга: {self.__dict__[min(greaterThanEqualK)]}")
        else:
            return print(f"{k}-с дээшгүй эсвэл тэнцүү хамгийн бага утгатай түлхүүр олдсонгүй.")
    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def __contains__(self, k):
        return k in self.__dict__.values()

dd = SortedMap()
dd["g"] = 1
dd["k"] = 2
dd["a"] = 5
dd["s"] = 8
dd["d"] = 9
dd["kl"] = 19

M = dd