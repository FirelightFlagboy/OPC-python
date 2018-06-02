import random
from getpass import getpass

def ft_hash(mdp):
	to_ascii = [ord(c) - ord('a') + 1 for c in mdp]
	print("to_ascii : ", to_ascii)
	weight = sum(to_ascii)
	print("weight : ", weight)
	return (mdp)

mdp = getpass("enter a mdp : ")
print("mdp before : ", mdp)
mdp = ft_hash(mdp.lower())
print("mdp after  : ", mdp)
