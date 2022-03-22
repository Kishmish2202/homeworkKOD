numbers = [7,4,5,10,7,14,22,4,2,3]
tmp_min = 0
tmp_max = 0

for i in numbers:
    if tmp_min == 0 and tmp_max ==0:
        tmp_min = i
        tmp_max = i
    elif i < tmp_min:
        tmp_min = i
    elif i > tmp_max:
        tmp_max = i

print(f'''
Список - {numbers}
Мин.число - {tmp_min}
Макс.число - {tmp_max}
''')


        
        
