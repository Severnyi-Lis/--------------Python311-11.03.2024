rainbow = {
    'violet',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet'}
rgb = {'red', 'green', 'blue'}
print(rainbow - rgb)
# То, что есть в радуге, но нет в rgb

letters = set('Мама мыла раму')
print(letters)
if 'м' in letters: 
    print('Есть такая буква!')
group321 = {
    'Ekaterina', 'Alex', 'Tanya', 'Nataly', 'Nikolay'}
group311 = {
    'Sergey', 'Ruslan', 'Tanya', 'Oleg',
    'Alex', 'Pavel', 'David'}
print('Все студенты: ', group321 | group311) # объединение

print('Студенты, которые перешли: ', group321 & group311)
# пересечение множеств

print('Студенты, не менявшие группу: ', group321 ^ group311)