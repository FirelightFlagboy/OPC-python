# -*-coding:utf-8 -*

import os
import re
from donnes import *
from solveur import *
from ft_file import *

def ft_check_map(map):
	if len(map) != 90:
		return False
	i = 0
	mod = 1
	while i < 90:
		while i < 10 * mod - 1:
			#print("char : {}: ord({}), i : {}".format(map[i], ord(map[i]), i))
			if map[i] != 'X' and ord(map[i]) < ord('0') and ord(map[i]) > ord('9'):
				return False
			i += 1
		#print("fin")
		mod += 1
		i += 1
	return True

def main():
	fcontent = ft_read_file(get_file_to_read_name())
	if ft_check_map(fcontent) == True:
		print("good")
		ft_start(fcontent)
	else:
		print("wrong")
		ft_write_file("map error", get_file_to_write_name())
	os.system("pause")
	pass

if __name__ == '__main__':
	main()