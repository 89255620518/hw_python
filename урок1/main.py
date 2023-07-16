# n = 1.89
# print(n)

# a = 5
# b = 5.89
# c = 'hello'
'''
print(a, '-', b, '-', c)
# или
print(f"{a} - {b} - {c}")
# или
print("{} - {} - {}". format(a, b, c))
'''
'''
# Ввод данных
print('Введите первую строку: ')
a = int(input())
b = int(input('Введите вторую строку: '))
print('a + b =',a + b)
'''
'''
a = 5.898989
b = 6.9898
print(round(a * b, 2))
'''
'''
iter  = 2
iter  += 4 # iter = iter + 4
iter  -= 5 # iter = iter - 5
iter  *= 5 # iter = iter * 5
iter  /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter  %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5
'''
'''
username = input('Введите имя: ')
if username == 'Маша':
    print('Ураа, это же Маша!')
elif username == 'Марина':
    print('Я так ждал вас, Марина')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)
'''
'''
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
else:
    print('Пожалуй')
    print('Хватить )')
print(i)
'''
# Замена break --> flag
'''
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:#Если остаток при делении n на 1 равен 0
        flag = False
        print(i)
    elif i > n // 2: #Делить числа не может превышать введенное число, деление на 2
        print(n)
        flag = False
    i += 1
'''
'''     
a = 'qwerty'

for i in a:
    print(i)
'''
'''
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
'''

# Строка
'''
text = 'СъЕШЬ еще этих МяГкИх французских булок'
# print(text[0])                       # c
# print(text[1])                       # ъ
# print(text[len(text)-1])             # k
# print(text[-1])                      # k
# print(text[-5])                      # б
# print(text[:])                       # СъЕШЬ еще этих МяГкИх французских булок
# print(text[:2])                      # съ
# print(text[len(text)-2:])            # ok
# print(text[2:9])                     # ешь еще
# print(text[6:-18])                   # еще этих мягких
# print(text[0:len(text):6])           # сеикакл
# print(text[::6])                     # сеикакл
# text = text[2:9]+text[-5]+text[:2]   # ЕШЬ ещебСъ
'''





