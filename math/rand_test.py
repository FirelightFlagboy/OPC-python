import random

print("random.random() :", random.random())
print("random.randrange(5, 10, 2) :", random.randrange(5, 10, 2))
print("random.randint(1, 6) :", random.randint(1, 6))
liste = ['a', 'b', 'k', 'p', 'i', 'w', 'z']
print("liste :", liste)
print("random.choice(liste) :", random.choice(liste))
tmp = liste[:]
print("random.shuffle(liste) :", random.shuffle(tmp))
print("liste :", tmp)

