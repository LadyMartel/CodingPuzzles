# String Problems

# ================================================================
# Number of occurences of substring s2 in string s1.
# Company: Clearslide 
# ================================================================
# s1 is the long string, s2 is the substring
def numOccurences(s1, s2):
	if len(s1) < len(s2) or len(s1) == 0 or len(s2) == 0:
		return 0
	# index of all the occurences of the first letter of the substring
	index = []
	count = 0

	for i in range(len(s1)):
		if s1[i] == s2[0]:
			index.append(i)

	for i in index:
		#python substring is apparently [start:end)
		if s1[i:i + len(s2)] == s2:
			count = count + 1

	print count
	
assert(numOccurences("hihi what is hi", "hi") == 3)
assert(numOccurences("abaaab","aab") == 1)
