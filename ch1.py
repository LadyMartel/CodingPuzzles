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
	if len(res) > len(s):
		return s
	return res 

assert(compressString("aabccaaaeee") == "a2b1c2a3e3")

# ================================================================
# 6. NxN matrix, each pixel is 4 bytes. Rotate image by 90 degrees
# ================================================================
# def rotateMatrix(m):
	# m is a list of lists
	# for xoffset in range(0, len(m)/2): # represents the 'layers'
# 		first = xoffset
# 		last = lem(m) - xoffset - 1

# 		for j in range(first, last):
# 			# save top
# 			temp = m[first][j]

# 			# left -> top
# 			m[first][j] = m[last-j][first]

# 			# bottom -> left
# 			m[last-j][first] = m[last-j][last-j]
			
# 			# right -> bottom
# 			m[first][last-j] = m[last-j][last-j]

# 			# top -> right
# 			m[first][last-j]


# TODO: LATER. I hate this problem
# assert(rotateMatrix([[1, 2],[3, 4])]) == [[3, 1],[4, 2]])


# ================================================================
# 7. MxN mmatrix, zero column and row if an element is zero
# ================================================================
def zeroColumnsAndRows(m):
	rowFlag = [0] * len(m[0]) # 1 if the row needs to be zero'd
	colFlag = [0] * len(m) 

	for i in range(len(m)):
		for j in range(len(m[0])):
			rowFlag[j] = rowFlag[j] or not m[i][j]
			colFlag[i] = colFlag[i] or not m[i][j]

	for i in range(len(m)):
		for j in range(len(m[0])):
			if rowFlag[j] or colFlag[i]:
				m[i][j] = 0
	return m

testMatrix = [	[1,1,1,1,0,1],
				[1,1,1,1,1,1],
				[1,0,1,1,1,1],
				[1,1,1,1,1,1]]

testResult = [	[0,0,0,0,0,0],
				[1,0,1,1,0,1],
				[0,0,0,0,0,0],
				[1,0,1,1,0,1]]

assert(zeroColumnsAndRows(testMatrix) == testResult)

# ================================================================
# 8. Given a function isSubstring, check if s2 is rotation of s1
# ================================================================
# HELPER: checks if s2 is a substring of s1
def isSubstring(s1, s2):
	# lol python
	return s2 in s1

assert(isSubstring("thisisgreat", "great") == True)

def isRotation(s1, s2): 
	return len(s1) == len(s2) and isSubstring(s2+s2, s1)

assert(isRotation("waterbottle", "bottlewater") == True)










