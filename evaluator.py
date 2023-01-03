# 
# MODIFY get_data() AS YOU LIKE.
# DO NOT SEND THIS FILE TO US

import random
random.seed(111)  #remove hash-sign to get randomization seed we will be using at evaluation
#                    (if you fix the seed you get always the same probabilty choice sequence)




def get_data():
	"""Get the initial state of the individuals & the environment"""
	       #[M, N,   D,   K, LAMBDA, MU,    universal_sta
	return [87, 93, 1, 9, 12, 0.13, [[(38, 40), 4, 'notmasked', 'notinfected'], [(85, 52), 5, 'notmasked', 'notinfected'], [(78, 30), 4, 'masked', 'infected'], [(21, 63), 7, 'notmasked', 'infected'], [(71, 50), 6, 'notmasked', 'notinfected'], [(5, 57), 1, 'notmasked', 'notinfected'], [(54, 34), 2, 'masked', 'infected'], [(87, 76), 4, 'notmasked', 'notinfected'], [(90, 78), 7, 'masked', 'notinfected'], [(4, 66), 7, 'notmasked', 'infected'], [(12, 10), 5, 'notmasked', 'infected'], [(84, 49), 3, 'notmasked', 'infected']]]