########################LOWERCASE##################################################
def tomuseg(a):
    b = ""
    for i in a:
        if 97 <= ord(i) <= 122:
            b += chr(ord(i) - 32) 
        else:
            b += i 
    return b

def jijiguseg(a):
    b = ""
    for i in a:
        if 65 <= ord(i) <= 90:
            b += chr(ord(i) + 32) 
        else:
            b += i 
    return b

def cap(a):
    return tomuseg(a[0])+ jijiguseg(a[1:])

def find(a,b):
    a=a.split()
    urt=0
    for i in a:
        if i == b:
            urt=urt+1
            break
        else:
            urt=urt+len(i)
    return urt

def tomuu(a):
    for i in a:
        if ord(i) < 65 or ord(i) > 90:
            return False
    return True

def jijiguu(a):
    for i in a:
        if ord(i) < 97 or ord(i) > 122:
            return False
    return True

def count(a, word):
    count = 0
    for i in range(len(a)):
        if a[i:i+len(word)] == word:
            count += 1
    return count



def split(s, kk=' '):
    a = []
    b = ''
    for i in s:
        if i == kk:
            if b != '':
                a.append(b)
                b = ''
        else:
            b += i
    if b != '':
        a.append(b)
    return a

def startswith(s, a):
    if len(a) > len(s):
        return False
    for i in range(len(a)):
        if s[i] != a[i]:
            return False
    return True

def endswith(s, b):
    if len(b) > len(s):
        return False
    for i in range(1, len(b) + 1):
        if s[-i] != b[-i]:
            return False
    return True

def replace(s, old, new):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result

def partition(s, sep):
    index = s.find(sep) 
    if index == -1:
        return (s, '', '')
    before = s[:index]
    separator = sep
    after = s[index+len(sep):]   
    return (before, separator, after)


