#coding:utf-8

from os import system

def ft_print_val_ascii():
	for i in range(0, 128):
		print("{0} '{1}'\t".format(i, chr(i)), end="")
		if (i + 1) % 8 == 0:
			print("\n", end="")

def main():
	ft_print_val_ascii()
	system("pause")

if __name__ == '__main__':
	main()