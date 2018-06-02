import hashlib

print(hashlib.algorithms_guaranteed)
chaine = input("enter a string  : ")
chaineb = chaine.encode()
hashing = hashlib.sha1(chaineb)
print(chaine, " to hash : ", hashing)
key = hashing.hexdigest()
print(key)

lock = True
while lock:
	entre = input("enter a mdp : ")
	entre = entre.encode()

	entre_hash = hashlib.sha1(entre).hexdigest()
	if entre_hash == key:
		lock = False
	else:
		print("wrong passwd")

print("mdp correct")
