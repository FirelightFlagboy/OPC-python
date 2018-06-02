# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    phone_number.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbenneto <f.benneto@student.42.fr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/04/13 19:49:57 by fbenneto          #+#    #+#              #
#    Updated: 2018/04/13 19:49:57 by fbenneto         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re

number = input("entrer a phone number :")
print("phone number that was enter is : {}".format(number))

regex = r"^0[0-9]([ -.]?[0-9]{2}){4}$"

if re.match(regex, number):
	print("{} is a phone number !".format(number))
else:
	print("{} is not a phone number !".format(number))
