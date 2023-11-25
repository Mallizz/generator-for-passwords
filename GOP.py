# generator of passwords/ генератор паролей
import random
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabet = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "g","f", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
x = random.choice((alphabet))
y = random.choice((alphabet))
z = random.choice((alphabet))
c = random.choice((alphabet))
v = random.choice((alphabet))

randomalphabet = [x, y, z, c, v]
randomalphabet1 = random.choice((randomalphabet))

q = random.choice((numbers))
w = random.choice((numbers))
e = random.choice((numbers))
r = random.choice((numbers))
t = random.choice((numbers))

print(x+y+z+c+v+q+w+e+r+t+randomalphabet1)