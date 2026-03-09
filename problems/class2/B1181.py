
a = int(input())

words = []

for i in range(a):
    words.append(input())

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for i in words:
    print(i)
