# Arrays and Strings

# ================================================================
# 1.Unique Characters
# ================================================================
# Assumption: ASCII characters

def hasUniqueChars(s):
	if len(s) > 256:
		return False

	seenChars = set()
	for c in s:
		if c in seenChars:
			return False
		seenChars.add(c)
	return True

# 1. Tests:
assert(hasUniqueChars("abcdefghijklmnop") == True)
assert(hasUniqueChars("") == True)
assert(hasUniqueChars("aa") == False)

# 1. Extension: No additional data structures
def hasUniqueCharsExtension(s):
	if len(s) > 256:
		return False
	# Array of 256 zeros because I don't know how to use bit vectors in python
	seenChars =	[0] * 256 
	for c in s:
		if seenChars[ord(c)]:
			return False
		else:
			seenChars[ord(c)] = 1
	return True

# 1. Extension tests:
assert(hasUniqueCharsExtension("abcdefghijklmnop") == True)
assert(hasUniqueCharsExtension("") == True)
assert(hasUniqueCharsExtension("aa") == False)

# ================================================================
# 2. in c
# ================================================================
# ================================================================
# 3. Permutations of each other
# ================================================================
def isPermutation(s1, s2):
	if not len(s1) == len(s2):
		return False
	seenChars = dict()
	i = 0
	for i in range(0, len(s1)): 
		if s1[i] in seenChars:
			seenChars[s1[i]] = seenChars[s1[i]] + 1
		else:
			seenChars[s1[i]] = 1

		if s2[i] in seenChars:
			seenChars[s2[i]] = seenChars[s2[i]] - 1
		else:
			seenChars[s2[i]] = -1

	for key, value in seenChars.iteritems():
		if value != 0:
			return False
	return True

# 3. Tests:
assert(isPermutation("abc", "cba") == True)
assert(isPermutation("abd", "adc") == False)

# ================================================================
# 4. Replace all spaces in a string with %20, in place 
# ================================================================
# TODO: later, probably in c++

# ================================================================
# 5. String compression that counts repeated characters 
# ================================================================
def compressString(s):
	i = 0 # keeps track of original string index
	j = 1 # keeps track of up till where the char repeats to
	res = s[0]
	while j < len(s):
		if s[i] == s[j]:
			j = j + 1
		else:
			res = res + str(j - i) + s[j]
			i = j 
			j = j + 1

	if j - i > 0:
		res = res + str(j -i)

	return res 

assert(compressionString("aabccaaaeee") == "a2b1c2a3e3")



