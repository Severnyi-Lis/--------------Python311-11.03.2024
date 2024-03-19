#сделать словарь,
#ключ - дата, значение - оценка.
#Оценки сделать случайным образом от 7 до 12.
#Вывести среднюю оценку за весь период.
#Вывести среднюю оценку за УКАЗАННЫЙ период.
#Например, сделайте даты от 1-го января каждый день 20 дней.
#"за указанный" - это с 4 по 9 января.
dictionary={ }
print(' Нет данных')
from datetime import datetime
dt_start=datetime.strptime(input('Введите дату дд.мм.гггг'),'%d.%m.%Y')
now=datetime.now()
while dt_start <= now: 
    from random import randint
    ocenka = randint(7, 12)
    dictionary[dt_start] = ocenka 
    dt_start=datetime.strptime(input('Введите  еще одну дату дд.мм.гггг'),'%d.%m.%Y')
sr_ocenka= 0
kol_ocenok= 0 
for lll in dictionary:
    kol_ocenok+=1
    sr_ocenka+=dictionary[lll]
    print(lll, dictionary[lll])
print('Общее количество оценок %4.1f'%kol_ocenok)
ttt=sr_ocenka/kol_ocenok   
print('Средняя оценка %4.1f '%ttt)





