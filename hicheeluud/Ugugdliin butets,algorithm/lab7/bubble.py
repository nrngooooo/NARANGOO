def bubble(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n-i-1):
            word1 = words[j]
            word2 = words[j+1]
            for k in range(min(len(word1), len(word2))):
                if ord(word1[k]) > ord(word2[k]):
                    words[j], words[j+1] = words[j+1], words[j]
                    break
                elif ord(word1[k]) < ord(word2[k]):
                    break
    return words


words = ["Баттөр", "Азжаргал", "Ариунзаяа", "Аззаяа", "азаа", "Ажаа","Баттамир"]
a = bubble(words)
print(a)