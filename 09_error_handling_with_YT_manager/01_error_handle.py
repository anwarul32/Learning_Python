
try:
    pass
except:
    pass
finally:
    pass

file = open('youtube.txt', 'w')

try:
    file.write('I learn Python with chaiaurcode')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('Anwarul learns python')