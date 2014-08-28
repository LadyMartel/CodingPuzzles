# Moderate mix of problems:
# ================================================================
# 1. swap a number in place
# ================================================================
def swapInPlace(a, b):
	a = a - b # a' = a - b
	b = a + b # b' = (a - b) + b = a
	a = b - a # a' = a - (a - b) = b

	return (a, b)

assert(swapInPlace(1,5) == (5, 1))

# ================================================================
# 2. Design an algo to see if someone has won tic tac toe
# ================================================================
# TODO: later

