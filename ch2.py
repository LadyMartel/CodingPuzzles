# Linked Lists

class ListNode:
	def __init__(self, x = None):
		self.val = x
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None 

	def toList(self):
		l = []
		cur = self.head  
		while cur:
			l.append(cur.val)
			cur = cur.next 
		return l

	def fromList(self, l):
		self.head = ListNode()
		cur = self.head
		for val in l:
			cur.val = val
			cur.next = ListNode()
			self.tail = cur 
			cur = cur.next

		self.tail.next = None

l = LinkedList()
l.fromList([1,2,3])

assert(l.toList() == [1,2,3])

# ================================================================
# 1.Remove Dups 
# ================================================================
def removeDuplicates(head):
	alreadySeen = set()
	prev = None
	cur = head 
	while cur:
		if cur.val in alreadySeen:
			# prev can never be None if cur.val is duplicate
			prev.next = cur.next
			cur = cur.next
		else:
			alreadySeen.add(cur.val)
			prev = cur 
			cur = cur.next 
	return head 

l = LinkedList()
l.fromList([1,1,2,3,4,4,4])
removeDuplicates(l.head)
assert(l.toList() == [1,2,3,4])

# ================================================================
# 2. find the kth to last element
# ================================================================
# Assumption: k = 0 -> last element
# k = n-1 element -> first element
def kthToLast(head, k):
	kth = head
	end = head
	prev = None 
	for i in range(k):
		end = end.next
	while end:
		prev = kth 
		kth = kth.next
		end = end.next
	return prev

assert(kthToLast(l.head, 0).val== 4)
assert(kthToLast(l.head, 3).val== 1)
assert(kthToLast(l.head, 1).val== 3)

# ================================================================
# 3. delete node given only access to that node
# ================================================================
# cannot delete last node of the list 

def deleteThisNode(n):
	if not n:
		return
	cur = n
	next = n.next
	if next:
		cur.val = next.val
		cur.next = n.next.next 

deleteThisNode(l.head.next.next) # delete 3
assert(l.toList() == [1,2,4])
deleteThisNode(l.head) # delete 1
assert(l.toList() == [2,4])


# ================================================================
# 4. partition the list around value x such that all nodes
# earlier are less than and all nodes greater than are later
# ================================================================

def partitionList(head, x):
	left = head
	right = head
	cur = head
	while cur:
		if cur == head:
			cur = cur.next
		elif cur.val < x:
			temp = cur.next
			cur.next = left
			left = cur
			cur = temp 
		else:
			right.next = cur
			cur = cur.next
			right = right.next
			right.next = None
	return left

l = LinkedList()
l.fromList([10,2,3,8,4,7])
l.head = partitionList(l.head, 5)
# print l.toList()
# TODO: write tests for this

# ================================================================
# 5. Two numbers represented by linked list
# digits are stored in reverse order
# Example: (7->1 -> 6) + (5 -> 9 -> 2) = 2->1-9
# 617 + 295 = 912
# ================================================================
# good enough for now
def addLinkedListNums(h1, h2):
	total = LinkedList()
	total.head = ListNode(0)
	cur = total.head
	carry = 0
	while h1 or h2:
		if h1:
			cur.val = cur.val + h1.val
			h1 = h1.next
		if h2:
			cur.val = cur.val + h2.val
			h2 = h2.next

		if cur.val >= 10:
			carry = (cur.val / 10)
			cur.val = cur.val - (cur.val / 10) * 10
		else:
			carry = 0

		cur.next = ListNode(carry)
		cur = cur.next
	return total 

l1 = LinkedList()
l1.fromList([7,1,6])

l2 = LinkedList()
l2.fromList([5, 9 , 2])

addLinkedListNums(l1.head, l2.head).toList()
# TODO: write tests

# ================================================================
# 6. Node at beginning of a loop in a circular linked list
# example: A -> B -> C -> D -> E -> C
# output: C
# ================================================================
# DUMB WAY:
def findStartOfCircle(head):
	alreadySeen = set()
	cur = head 
	while cur:
		if cur in alreadySeen:
			return cur
		else:
			alreadySeen.add(cur)
		cur = cur.next

	return None


l1 = LinkedList()
l1.fromList([1,2,3,4,5,6,7])
l1.tail.next = l1.head.next.next.next

assert(findStartOfCircle(l1.head).val == 4)

# ================================================================
# 7.Check if a linked list is a palindrome 
# ================================================================
def isPalindrome(head):
	(res, _) = isPalindromeHelper(head, head)
	return res 


def isPalindromeHelper(start, end):
	if not end.next:
		# start poppin'
		return (start.val == end.val, start.next)
	else:
		(res, cur) = isPalindromeHelper(start, end.next)
		return  (cur.val == end.val and res, cur.next)


l1 = LinkedList()
l1.fromList([1,2,2,1])
assert(isPalindrome(l1.head) == True)
l1.fromList([1,2,3,2,1])
assert(isPalindrome(l1.head) == True)
l1.fromList([1,2,3,1])
assert(isPalindrome(l1.head) == False)



