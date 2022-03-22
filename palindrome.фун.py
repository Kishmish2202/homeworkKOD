def palindrome(s):
    if s == s [::-1]:
        return True
    return False

rr = input('Введите слово:')

if palindrome(rr):
    print('Является.')
else:
    print('Не является')
