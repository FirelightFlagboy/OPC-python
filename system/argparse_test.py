import argparse

parser = argparse.ArgumentParser(description="square the number x")

parser.add_argument("x", help="le nombre a mettre au carré", type=int)
parser.add_argument("-v", "--verbose", action="store_true", default=0
	help="augmente la verbosité")

arg = parser.parse_args()
print("le nm a mettre au carre est =", arg.x)
x = arg.x
sqr_x = x ** 2

if arg.verbose:
	print("{} ^ 2 = {}".format(x, sqr_x))
else:
	print(">>", sqr_x)
