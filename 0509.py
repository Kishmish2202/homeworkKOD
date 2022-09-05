text = input('Введите текст...')
w = {}

for i in text:
    i = i.lower()
    if i not in w:
        w[i] = 1
    else:
        w[i] += 1

maximal = max(w.values())

for k in w.keys():
    if w[k] == maximal:
        maximal = k, w[k]
        break
print(f'Часто употребляли слово: {maximal[0]} - {maximal[1]}')